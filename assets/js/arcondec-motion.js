/*
 * Movimiento Arcondec — GSAP + ScrollTrigger + SplitText.
 *
 * Por qué existe
 * --------------
 * El template trae WOW.js + animate.css, pero solo lo aplica a 193 elementos de
 * todo el sitio (y ninguno en proyectos, contacto ni blog): el resto aparece de
 * golpe. Además animate.css desplaza los bloques el 100% de su alto, un salto muy
 * brusco al lado del resto de la interfaz.
 *
 * Este archivo sustituye a WOW por un sistema único, y se apoya en la estructura
 * que ya existe —las filas y columnas del grid de Bootstrap— para cubrir las 28
 * páginas sin marcar nada en el HTML y sin tocar style.css ni main.js.
 *
 * Qué hace, de más a menos visible
 * --------------------------------
 * 1. Los titulares grandes entran línea a línea, cada una subiendo por debajo de
 *    una máscara. Es el gesto que carga el peso: el resto del bloque lo acompaña.
 * 2. Las columnas del grid aparecen con fundido y 32px de subida, escalonadas.
 * 3. Las fotos de las tarjetas hacen un zoom de salida de 1.08 a 1; las fotos
 *    grandes de portada se descubren con una cortina (clip-path).
 * 4. El ícono redondo de cada tarjeta de servicio entra con un rebote corto.
 * 5. El hero lleva su propia línea de tiempo por diapositiva, más un zoom lento
 *    sobre la foto.
 * 6. Parallax en los fondos fotográficos y barra de progreso de lectura arriba.
 *
 * Reglas que respeta
 * ------------------
 * - Si GSAP no cargó, no toca nada y WOW sigue funcionando como antes.
 * - Con `prefers-reduced-motion: reduce` no registra ninguna aparición por
 *   scroll —ni la suya ni la del template— y la página se queda quieta. Única
 *   excepción: los botones del hero siguen montados, sin avance automático y
 *   sin transición, porque son el único camino a las láminas 2 y 3.
 * - Todo movimiento automático de la portada (hero cada 11 s, cinta de logos
 *   cada 3 s) se detiene con el botón de pausa del hero, como pide WCAG 2.2.2.
 * - Nada se oculta hasta que la página termina de cargar y las fuentes están
 *   listas, así que un fallo previo nunca deja contenido invisible.
 * - No entra en el header, los carruseles ni los botones flotantes: ahí manda el
 *   template.
 * - Para excluir un bloque a mano: data-arc-motion="off".
 */
(function (window, document) {
    'use strict';

    var gsap = window.gsap;
    var ScrollTrigger = window.ScrollTrigger;
    var SplitText = window.SplitText;

    // Sin GSAP se sale sin tocar nada: WOW.js sigue siendo el sistema del sitio.
    if (!gsap || !ScrollTrigger) { return; }

    gsap.registerPlugin(ScrollTrigger);
    if (SplitText) { gsap.registerPlugin(SplitText); }

    /* ==========================================================================
       1. El movimiento del template queda fuera
       --------------------------------------------------------------------------
       main.js arranca WOW dentro de su `jQuery(document).on('ready')`, y este
       archivo se ejecuta antes (va al final del <body>, DOMContentLoaded todavía
       no ha ocurrido). Al quitar aquí la clase `wow`, main.js no encuentra a
       quién animar: un solo sistema en la página, sin nada moviéndose dos veces.

       El hero de la portada ya no es el slider del template (.hero-slider), así
       que no queda ningún [data-animation] que desenganchar: lo mueve heroSlides.
       ========================================================================== */
    var WOW_CLASSES = ['wow', 'animated', 'fadeInUp', 'fadeInLeft', 'fadeInRight', 'fadeInDown'];

    function unhookTemplateMotion() {
        var wowNodes = document.querySelectorAll('.wow');
        var i, j;
        for (i = 0; i < wowNodes.length; i++) {
            for (j = 0; j < WOW_CLASSES.length; j++) {
                wowNodes[i].classList.remove(WOW_CLASSES[j]);
            }
            wowNodes[i].removeAttribute('data-wow-duration');
            wowNodes[i].removeAttribute('data-wow-delay');
        }
    }

    unhookTemplateMotion();

    /* Con animaciones reducidas la página se queda quieta: el template ya no
       anima nada y aquí no se registra ninguna aparición por scroll.

       La única excepción es el hero. Sus tres láminas se apilan y el CSS solo
       enseña la primera; si nadie las rota, las láminas 2 y 3 —con su titular,
       su párrafo y sus CTAs— no hay forma de verlas. Eso ya no es renunciar a
       una animación, es esconder contenido a quien pidió menos movimiento.
       Se monta el hero sin avance automático y con cambios instantáneos: los
       botones anterior/siguiente quedan como único mando, y nada se mueve
       hasta que el visitante lo pide. */
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        safely('heroSlides (movimiento reducido)', function () {
            heroSlides({ quieto: true, automatico: false });
        });
        return;
    }

    /* ==========================================================================
       2. Ajustes
       ========================================================================== */
    var SKIP = [
        'header',                 // cabecera y menú: los mueve main.js
        '.preloader',
        '.slick-list',            // dentro de un carrusel manda slick
        '.page-title-area',       // sobre la línea de flotación: entra al cargar
        '.back-to-top',
        '.whatsapp-float',
        '[data-arc-motion="off"]'
    ].join(', ');

    var EASE = 'power3.out';
    var RISE = 32;
    var STAGGER = 0.09;

    // clamp() ata el punto de disparo al recorrido real de la página. Sin él, en
    // una página corta un bloque que se quede en el último 10% de la pantalla no
    // llegaría nunca a su marca —no hay scroll que lo suba— y se quedaría
    // invisible para siempre.
    var START = 'clamp(top 90%)';

    // Un titular se trata como "de portada" —y se descompone en líneas— si es
    // grande, no lleva etiquetas dentro y tiene texto suficiente. Así entran los
    // de sección (48px) y el del hero (80px), y quedan fuera los de tarjeta
    // (22px) y cosas como la caja «30+», que son tres caracteres.
    var HEADING_SEL = 'h1.title, h2.title, h3.title';
    var HEADING_MIN_SIZE = 32;
    var HEADING_MIN_CHARS = 8;

    /* ==========================================================================
       3. Utilidades
       ========================================================================== */
    function isColumn(el) {
        return el.nodeType === 1 &&
            typeof el.className === 'string' &&
            /(^|\s)col(-[\w-]+)?(\s|$)/.test(el.className);
    }

    function isVisible(el) {
        return el.offsetParent !== null;
    }

    /* --------------------------------------------------------------------------
       Lo que ya se ve al cargar entra solo, sin esperar a un scroll.

       Un bloque que al cargar la página ya está por encima de la línea de disparo
       tiene su marca en 0 (clamp la ata al recorrido). Y ScrollTrigger no
       considera «entrada» quedarse quieto en el punto de disparo: hace falta
       cruzarlo. Resultado: todo lo de la primera pantalla se quedaba invisible
       hasta que el usuario movía la rueda —en la portada no se notaba porque el
       hero ocupa 1275px y no hay nada más arriba, pero en las páginas interiores
       el contenido bajo el banner salía en blanco—.

       Estos bloques se animan directamente, encadenados, y se leen como la
       presentación de la página. La cuenta sirve igual si se entra a mitad de
       página (un enlace con ancla, una recarga): se mide contra la ventana real,
       así que «ya visible» significa visible de verdad, no «está arriba del todo».
       -------------------------------------------------------------------------- */
    var introContador = 0;

    // El umbral es la ventana entera, no la línea de disparo: cualquier cosa que
    // asome aunque sea por el borde inferior entra sola. Un bloque justo debajo de
    // la línea se quedaría en blanco a la vista del usuario hasta que moviera la
    // rueda, y ese es exactamente el efecto que hay que evitar.
    function yaEnPantalla(el) {
        return el.getBoundingClientRect().top < window.innerHeight;
    }

    function lineaDeTiempo(trigger, vars) {
        var opciones = vars || {};

        if (yaEnPantalla(trigger)) {
            opciones.delay = (opciones.delay || 0) + 0.1 * Math.min(introContador++, 6);
        } else {
            opciones.scrollTrigger = { trigger: trigger, start: START, once: true };
        }

        return gsap.timeline(opciones);
    }

    function displayHeadingIn(root) {
        var candidates = root.querySelectorAll(HEADING_SEL);
        for (var i = 0; i < candidates.length; i++) {
            var h = candidates[i];
            if (h.children.length) { continue; }
            if (h.textContent.trim().length < HEADING_MIN_CHARS) { continue; }
            if (parseFloat(window.getComputedStyle(h).fontSize) < HEADING_MIN_SIZE) { continue; }
            return h;
        }
        return null;
    }

    // Todo lo que acompaña al titular dentro de su columna: se sube por los
    // ancestros hasta la columna recogiendo los hermanos de cada nivel, así el
    // párrafo y los botones entran detrás del titular aunque estén envueltos.
    function companionsOf(column, heading) {
        var out = [];
        var node = heading;
        while (node && node !== column && node.parentElement) {
            var siblings = node.parentElement.children;
            for (var i = 0; i < siblings.length; i++) {
                if (siblings[i] !== node && isVisible(siblings[i])) { out.push(siblings[i]); }
            }
            node = node.parentElement;
        }
        return out.sort(function (a, b) {
            return (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING) ? -1 : 1;
        });
    }

    // Las líneas se envuelven en una máscara con overflow, de modo que basta con
    // desplazarlas: no hace falta opacidad y el borde del recorte se ve limpio.
    // Se deshace el split al terminar para que el titular vuelva a ser texto
    // normal y reflote solo al cambiar el ancho de la ventana.
    //
    // El recorte de la máscara cae justo en la caja de línea, y con interlineados
    // apretados (el titular del hero va a 1.08) los trazos que bajan —la «g», la
    // «j», la «p»— se salen de ella un par de píxeles y quedan cortados. La
    // máscara necesita ese aire, pero NO puede crecer: partir un titular no debe
    // cambiar el alto de la página. Si cambia, los puntos de disparo que
    // ScrollTrigger ya calculó dejan de corresponder con el recorrido real y el
    // último bloque de la página puede quedar fuera de alcance para siempre.
    // El margen negativo devuelve exactamente lo que suma el relleno.
    var MASK_ROOM = '0.09em';

    function splitLines(heading) {
        if (!SplitText) { return null; }

        var split;
        try {
            split = new SplitText(heading, { type: 'lines', mask: 'lines', linesClass: 'arc-line' });
        } catch (err) {
            return null;
        }

        split.lines.forEach(function (line) {
            var mask = line.parentElement;
            if (!mask || mask === heading) { return; }
            mask.style.paddingBottom = MASK_ROOM;
            mask.style.marginBottom = '-' + MASK_ROOM;
        });

        return split;
    }

    // Cualquier cosa que cambie el alto del documento después de haber creado los
    // disparadores —una foto que termina de cargar, un titular que se recompone—
    // deja los puntos de disparo desfasados. Se recalculan una sola vez, agrupando
    // las llamadas seguidas.
    var refreshQueued = false;

    function scheduleRefresh() {
        if (refreshQueued) { return; }
        refreshQueued = true;
        gsap.delayedCall(0.35, function () {
            refreshQueued = false;
            ScrollTrigger.refresh();
        });
    }

    function revertSplit(split) {
        if (!split) { return; }
        split.revert();
        scheduleRefresh();
    }

    // Garantía de última instancia. El punto de disparo de un bloque se calcula
    // una vez, y entre medias la página puede encoger —al recomponerse un titular,
    // al cargar una foto—; si el bloque que peor margen tenía queda por encima del
    // nuevo final del scroll, no habría forma de alcanzarlo. Cuando el usuario toca
    // fondo, cualquier bloque que siga sin haber entrado se muestra sin más. No
    // depende de ningún cálculo de altura: si estás al final de la página, no queda
    // nada por revelar.
    function rescuePending() {
        if (window.scrollY < ScrollTrigger.maxScroll(window) - 2) { return; }

        ScrollTrigger.getAll().forEach(function (trigger) {
            if (trigger.vars.scrub || trigger.progress > 0) { return; }
            if (trigger.animation) { trigger.animation.progress(1); }
        });
    }

    /* ==========================================================================
       4. Filas del grid: la unidad de aparición
       ========================================================================== */
    function collectRows() {
        var rows = document.querySelectorAll('.row');
        var groups = [];
        var claimed = [];
        var i, c, k;

        for (i = 0; i < rows.length; i++) {
            var row = rows[i];
            if (row.closest(SKIP)) { continue; }

            // Una fila anidada dentro de una columna ya animada se movería dos
            // veces: se deja fuera y viaja con su columna.
            var nested = false;
            for (c = 0; c < claimed.length; c++) {
                if (claimed[c].contains(row)) { nested = true; break; }
            }
            if (nested) { continue; }

            var cols = [];
            for (k = 0; k < row.children.length; k++) {
                // Oculto (pestaña inactiva, columna solo-móvil): no se le aplica
                // estado inicial, para no dejarlo invisible.
                //
                // El SKIP se comprueba también columna por columna, no solo en la
                // fila: si no, marcar una columna con data-arc-motion="off" no
                // sirve de nada —queda dentro de una fila sin marcar y se anima
                // igual—, y el bloque termina con dos animaciones peleándose por
                // las mismas propiedades. Es lo que pasaba con las tarjetas de
                // artículo, que traen la suya propia.
                if (isColumn(row.children[k]) && isVisible(row.children[k]) &&
                    !row.children[k].closest(SKIP)) {
                    cols.push(row.children[k]);
                }
            }

            // Filas sin columnas propias: el carrusel de servicios de la portada
            // cuelga directo de la fila, porque slick mete su propio envoltorio.
            if (!cols.length) {
                if (!isVisible(row) || !row.children.length) { continue; }
                groups.push({ row: row, cols: [row] });
                claimed.push(row);
                continue;
            }

            groups.push({ row: row, cols: cols });
            claimed = claimed.concat(cols);
        }

        return groups;
    }

    function revealRows() {
        collectRows().forEach(function (group) {
            var plain = [];

            group.cols.forEach(function (col) {
                var heading = displayHeadingIn(col);
                if (heading) {
                    revealEditorial(col, heading);
                } else {
                    plain.push(col);
                }
            });

            if (!plain.length) { return; }

            // Una fila del grid no es un renglón en pantalla: seis tarjetas van en
            // dos renglones de tres en escritorio y en seis apilados en el móvil,
            // donde la fila entera mide varias pantallas. Disparando por fila, en
            // el móvil las seis arrancarían a la vez y las últimas se moverían muy
            // por debajo del borde inferior: al llegar a ellas ya estarían puestas.
            // Agrupando por renglón visual, cada breakpoint hace lo suyo solo.
            visualBands(plain).forEach(function (band) {
                var tl = lineaDeTiempo(band[0]);

                tl.from(band, {
                    y: RISE,
                    opacity: 0,
                    duration: 0.8,
                    ease: EASE,
                    stagger: band.length > 1 ? STAGGER : 0,
                    clearProps: 'transform,opacity'
                });

                decorate(tl, band);
            });
        });
    }

    // Reparte las columnas por la altura a la que están: las que comparten borde
    // superior (con 12px de tolerancia, por los márgenes escalonados del template)
    // van juntas y entran escalonadas.
    function visualBands(cols) {
        var bands = [];

        cols.forEach(function (col) {
            var top = Math.round(col.getBoundingClientRect().top);
            var band = null;
            for (var i = 0; i < bands.length; i++) {
                if (Math.abs(bands[i].top - top) <= 12) { band = bands[i]; break; }
            }
            if (!band) { band = { top: top, cols: [] }; bands.push(band); }
            band.cols.push(col);
        });

        return bands.map(function (b) { return b.cols; });
    }

    // Columna con titular de portada: manda el titular, línea a línea, y el resto
    // del bloque entra un pelín después. El bloque completo no se funde, para que
    // no compitan dos gestos sobre lo mismo.
    function revealEditorial(column, heading) {
        var split = splitLines(heading);
        var companions = companionsOf(column, heading);

        var tl = lineaDeTiempo(column, {
            onComplete: function () { revertSplit(split); }
        });

        if (split && split.lines.length) {
            tl.from(split.lines, {
                yPercent: 115,
                duration: 0.9,
                ease: EASE,
                stagger: 0.08
            }, 0);
        } else {
            tl.from(heading, { y: RISE, opacity: 0, duration: 0.8, ease: EASE, clearProps: 'transform,opacity' }, 0);
        }

        if (companions.length) {
            tl.from(companions, {
                y: 24,
                opacity: 0,
                duration: 0.7,
                ease: EASE,
                stagger: 0.08,
                clearProps: 'transform,opacity'
            }, 0.18);
        }

        decorate(tl, [column]);
    }

    /* ==========================================================================
       5. Detalles que entran con su bloque
       --------------------------------------------------------------------------
       Van en la misma línea de tiempo que el bloque, no en un ScrollTrigger
       aparte: así el gesto se lee como uno solo y no como tres cosas sueltas.
       ========================================================================== */
    // Dentro de un carrusel no se toca nada. Slick, al cruzar un punto de ruptura,
    // se destruye y vuelve a clonar sus diapositivas a partir de los originales,
    // copiando el estilo en línea que GSAP les haya dejado puesto. Los clones no
    // pertenecen a ningún tween, así que el `clearProps` del final nunca les llega
    // y se quedarían con `opacity: 0` para siempre. La fila entera sigue
    // apareciendo; lo que no se decora es su contenido.
    function inCarousel(el) {
        return !!el.closest('.slick-slider, .slick-list, .slick-track');
    }

    function decorate(timeline, roots) {
        var photos = [];
        var icons = [];

        roots.forEach(function (root) {
            var images = root.querySelectorAll('img');
            for (var i = 0; i < images.length; i++) {
                if (inCarousel(images[i])) { continue; }
                // El zoom de salida solo cabe donde el contenedor recorta; si no,
                // la foto se saldría de su caja.
                var parent = images[i].parentElement;
                if (parent && window.getComputedStyle(parent).overflow === 'hidden') {
                    photos.push(images[i]);
                }
            }
            var circles = root.querySelectorAll('.service-2-item .icon, .sub-2-item > img');
            for (var j = 0; j < circles.length; j++) {
                if (!inCarousel(circles[j])) { icons.push(circles[j]); }
            }
        });

        if (photos.length) {
            timeline.from(photos, {
                scale: 1.08,
                duration: 1.2,
                ease: EASE,
                stagger: photos.length > 1 ? 0.06 : 0,
                clearProps: 'transform'
            }, 0);
        }

        if (icons.length) {
            timeline.from(icons, {
                scale: 0.55,
                opacity: 0,
                duration: 0.6,
                ease: 'back.out(1.8)',
                stagger: icons.length > 1 ? 0.06 : 0,
                clearProps: 'transform,opacity'
            }, 0.2);
        }
    }

    /* ==========================================================================
       6. Fotos grandes de portada: cortina en vez de fundido
       --------------------------------------------------------------------------
       El recorte va sobre la <img>, no sobre su contenedor: en «Nosotros» el
       contenedor no recorta y lleva encima la caja «30+ Años» en posición
       absoluta, que una máscara sobre el padre se comería. Se lee el radio real
       de la imagen para que las esquinas no se cuadren durante la cortina.
       ========================================================================== */
    var FEATURE_MEDIA = [
        '.about-2-thumb .thumb img',
        '.about-2-thumb .thumb-2 img',
        '.testimonial-11-thumb img',
        '.case-thumb img'
    ].join(', ');

    function revealFeatureMedia() {
        var nodes = document.querySelectorAll(FEATURE_MEDIA);

        for (var i = 0; i < nodes.length; i++) {
            var img = nodes[i];
            if (img.closest(SKIP) || !isVisible(img)) { continue; }

            var radius = window.getComputedStyle(img).borderRadius;
            var round = (radius && radius !== '0px') ? ' round ' + radius : '';

            // Misma regla que el resto: si ya se ve al cargar, se descubre sola.
            var destino = {
                clipPath: 'inset(0% 0% 0% 0%' + round + ')',
                duration: 1.1,
                ease: EASE,
                clearProps: 'clipPath'
            };
            if (yaEnPantalla(img)) {
                destino.delay = 0.1 * Math.min(introContador++, 6);
            } else {
                destino.scrollTrigger = { trigger: img, start: START, once: true };
            }

            gsap.fromTo(img, { clipPath: 'inset(0% 0% 100% 0%' + round + ')' }, destino);
        }
    }

    /* ==========================================================================
       6b. Mapa de cobertura: fundido con zoom, nunca cortina
       --------------------------------------------------------------------------
       El mapa no es una foto: es un gráfico con cajas de etiquetas flotando
       alrededor del contorno. Una cortina las va cercenando mientras avanza y
       durante ese segundo la sección se ve rota, justo donde el mensaje es
       cobertura y solidez. Con opacidad y escala entra completo, sin recortes.
       Su bloque lleva data-arc-motion="off" para que ni revealRows ni
       revealFeatureMedia lo toquen: aquí se anima la <img> a mano y por eso
       esta función no consulta SKIP.
       ========================================================================== */
    // El mapa se dispara más tarde que el resto. Con el START general
    // —clamp(top 90%)— la animación arranca cuando la imagen apenas asoma por
    // el borde inferior: para cuando el usuario la tiene enfrente, ya terminó,
    // y el movimiento se percibe como si no existiera. A 75% el mapa ya entró
    // un cuarto de pantalla y la entrada se ve completa.
    var START_MAPA = 'clamp(top 75%)';

    function revealMap() {
        var nodes = document.querySelectorAll('.arc-map img');

        for (var i = 0; i < nodes.length; i++) {
            var img = nodes[i];
            if (!isVisible(img)) { continue; }

            var destino = {
                autoAlpha: 1,
                scale: 1,
                y: 0,
                duration: 1.2,
                ease: EASE,
                clearProps: 'transform,opacity,visibility'
            };
            if (yaEnPantalla(img)) {
                destino.delay = 0.1 * Math.min(introContador++, 6);
            } else {
                destino.scrollTrigger = { trigger: img, start: START_MAPA, once: true };
            }

            gsap.fromTo(img, { autoAlpha: 0, scale: 0.90, y: 64 }, destino);
        }
    }

    /* ==========================================================================
       6c. Carrusel de logos de clientes
       --------------------------------------------------------------------------
       Avanza de un logo a la vez cada 3s, no en cinta continua: un logo quieto
       durante unos segundos se lee, uno en movimiento perpetuo no. Va con slick
       —que el sitio ya carga— en lugar de con GSAP, porque slick resuelve solo
       el bucle infinito, el número de visibles por tamaño de pantalla y la
       pausa al pasar el cursor.

       rtl: true es lo que hace que la tira viaje hacia la derecha. Slick no
       tiene autoplay inverso; en modo rtl el "siguiente" empuja el contenido en
       sentido contrario, que es justo lo pedido. Como efecto lateral invierte el
       orden de aparición de los logos, cosa que aquí da igual.

       Si slick o jQuery no cargan, la función se sale y el CSS deja los logos en
       una fila con desplazamiento manual: la sección nunca queda vacía. Lo mismo
       con movimiento reducido, donde esta función ni se llama.

       El botón de pausa del hero también detiene esta cinta (ver heroSlides):
       son los dos movimientos automáticos de la portada y WCAG 2.2.2 pide poder
       parar todos, no uno. Por eso la pista se guarda en `logosPista`.
       ========================================================================== */
    var logosPista = null;

    function logoCarousel() {
        var jq = window.jQuery;
        var pista = document.querySelector('.arc-logos');
        if (!jq || !pista || !jq.fn || !jq.fn.slick) { return; }
        if (pista.children.length < 2 || pista.classList.contains('slick-initialized')) { return; }

        logosPista = pista;

        jq(pista).slick({
            slidesToShow: 5,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 3000,
            speed: 700,
            infinite: true,
            arrows: false,
            dots: false,
            pauseOnHover: true,
            // Al tabular hasta un logo la cinta se detiene: sin esto el enlace
            // enfocado se va de la pantalla y el foco queda en un sitio invisible.
            pauseOnFocus: true,
            rtl: true,
            cssEase: 'cubic-bezier(0.4, 0, 0.2, 1)',
            responsive: [
                { breakpoint: 1200, settings: { slidesToShow: 5 } },
                { breakpoint: 992, settings: { slidesToShow: 4 } },
                { breakpoint: 768, settings: { slidesToShow: 3 } },
                { breakpoint: 576, settings: { slidesToShow: 2 } }
            ]
        });

        scheduleRefresh();
    }

    /* ==========================================================================
       6d. Tarjetas de artículo: entrada en dos capas
       --------------------------------------------------------------------------
       Estas tarjetas ya entraban con el escalonado genérico de columnas, pero no
       se percibía: el disparo general —clamp(top 90%)— arranca cuando la fila
       apenas asoma por el borde inferior, así que la animación termina antes de
       que el usuario la tenga enfrente. Aquí se dispara al 80%.

       Las tarjetas de cada renglón se deslizan 48px hacia arriba con fundido, y
       lo hacen a la vez, sin escalonar. El escalonado insinúa un orden de lectura
       —primero esta, luego esta— y aquí los tres artículos valen igual.

       Las columnas se marcan con data-arc-motion="off" ANTES de que corra
       revealRows, que es quien las animaría por su cuenta: sin eso las tarjetas
       llevarían dos animaciones encima peleándose por la misma propiedad.
       Por eso esta función va primero en start().
       ========================================================================== */
    var START_TARJETAS = 'clamp(top 80%)';

    function revealArticleCards() {
        var cards = document.querySelectorAll('.article-11-item');
        if (!cards.length) { return; }

        var filas = [];
        for (var i = 0; i < cards.length; i++) {
            var card = cards[i];
            if (card.closest(SKIP) || !isVisible(card)) { continue; }
            var col = card.closest('[class*="col-"]');
            var fila = col && col.parentElement;
            if (!col || !fila) { continue; }
            if (filas.indexOf(fila) === -1) { filas.push(fila); }
        }

        filas.forEach(function (fila) {
            var cols = [];
            for (var j = 0; j < fila.children.length; j++) {
                var col = fila.children[j];
                if (!col.querySelector('.article-11-item') || !isVisible(col)) { continue; }
                col.setAttribute('data-arc-motion', 'off');
                cols.push(col);
            }
            if (!cols.length) { return; }

            // Misma razón que en revealRows: en la página de Blog las 12 tarjetas
            // cuelgan de UNA sola fila del código, pero en pantalla son cuatro
            // renglones. Disparando por fila, las ocho de abajo terminarían su
            // animación muy por debajo del borde inferior y al llegar a ellas ya
            // estarían puestas. Se agrupan por la altura real a la que están.
            visualBands(cols).forEach(function (band) {
                var opciones = {};
                if (yaEnPantalla(band[0])) {
                    opciones.delay = 0.1 * Math.min(introContador++, 6);
                } else {
                    opciones.scrollTrigger = { trigger: band[0], start: START_TARJETAS, once: true };
                }

                // Sin escalonado: las tarjetas del renglón entran a la vez. Se leen
                // como un bloque —tres artículos del mismo nivel— en vez de como
                // una lista con jerarquía, que es lo que sugiere el escalonado.
                gsap.timeline(opciones).fromTo(band,
                    { autoAlpha: 0, y: 48 },
                    {
                        autoAlpha: 1, y: 0, duration: 0.9, ease: EASE,
                        clearProps: 'transform,opacity,visibility'
                    }, 0);
            });
        });
    }

    /* ==========================================================================
       7. Banner de las páginas interiores: entra al cargar, no al hacer scroll
       ========================================================================== */
    function revealBanner() {
        var content = document.querySelector('.page-title-area .page-title-content');
        if (!content) { return; }

        var heading = displayHeadingIn(content);
        var split = heading ? splitLines(heading) : null;
        var rest = [];
        for (var i = 0; i < content.children.length; i++) {
            if (content.children[i] !== heading) { rest.push(content.children[i]); }
        }

        var tl = gsap.timeline({
            onComplete: function () { revertSplit(split); }
        });

        if (split && split.lines.length) {
            tl.from(split.lines, { yPercent: 115, duration: 0.9, ease: EASE, stagger: 0.08 }, 0);
        } else if (heading) {
            tl.from(heading, { y: 24, opacity: 0, duration: 0.8, ease: EASE, clearProps: 'transform,opacity' }, 0);
        }

        if (rest.length) {
            tl.from(rest, { y: 18, opacity: 0, duration: 0.7, ease: EASE, stagger: 0.1, clearProps: 'transform,opacity' }, 0.2);
        }
    }

    /* ==========================================================================
       8. Parallax en los fondos fotográficos
       --------------------------------------------------------------------------
       Solo donde el fondo es una foto sola. Los fondos con degradado encima
       (servicios) llevan dos capas y una sola background-position las movería a
       las dos, dejando el degradado sin cubrir los bordes.
       ========================================================================== */
    function parallaxBackgrounds() {
        var backgrounds = document.querySelectorAll('.section__bg');

        for (var i = 0; i < backgrounds.length; i++) {
            var bg = backgrounds[i];
            var image = window.getComputedStyle(bg).backgroundImage;
            if (image.indexOf('url(') !== 0 || image.split(/,(?![^(]*\))/).length !== 1) { continue; }

            gsap.fromTo(bg,
                { backgroundPosition: '50% 42%' },
                {
                    backgroundPosition: '50% 58%',
                    ease: 'none',
                    scrollTrigger: {
                        trigger: bg.parentElement,
                        start: 'top bottom',
                        end: 'bottom top',
                        scrub: 0.4
                    }
                }
            );
        }
    }

    /* ======================================================================
       9. Hero-tarjeta de portada: tres láminas con controles
       ----------------------------------------------------------------------
       Las láminas se funden cada 11 s: la foto activa respira con un zoom
       lento (Ken Burns), el panel de texto sale hacia arriba y el entrante
       sube en cascada; el contador 01/03 acompaña.

       Los botones anterior/pausa/siguiente no son decoración:

       · WCAG 2.2.2 («Pausar, detener, ocultar») exige poder detener cualquier
         movimiento automático que dure más de 5 segundos. Once no son cinco.
       · Con `prefers-reduced-motion` no hay avance automático, y sin botones
         las láminas 2 y 3 quedarían inalcanzables: el CSS solo enseña la
         primera. Eso no es perder una animación, es perder contenido. Por eso
         esta función SÍ corre en ese modo —es la única que lo hace—, con
         `quieto`, que cambia de lámina sin transición.

       Sin GSAP el archivo entero se sale antes y el CSS deja la primera lámina
       fija y completa: nada queda oculto.
       ====================================================================== */
    function heroSlides(opciones) {
        var conf = opciones || {};
        var quieto = !!conf.quieto;          // sin transiciones ni Ken Burns
        var automatico = conf.automatico !== false;

        var section = document.querySelector('.arc-hero');
        if (!section) { return; }
        var slides = section.querySelectorAll('.arc-hero-slide');
        if (slides.length < 2) { return; }
        var countEl = section.querySelector('.arc-hero-count-n');
        var toggle = section.querySelector('[data-arc-hero="toggle"]');
        var prev = section.querySelector('[data-arc-hero="prev"]');
        var next = section.querySelector('[data-arc-hero="next"]');

        // Tiempo que cada lámina permanece en pantalla, en milisegundos.
        // De esos, ~1.15 s se van en la entrada del panel, así que el tiempo
        // real de lectura es INTERVAL - 1150. La lámina más larga son 47
        // palabras: a 11 s quedan ~9.8 s de lectura. Si se alarga el copy,
        // subir este número. El zoom Ken Burns se ajusta solo.
        var INTERVAL = 11000;
        var current = 0;
        var busy = false;
        var timer = null;
        var pausado = !automatico;

        function kenBurns(slide) {
            if (quieto) { return; }
            var img = slide.querySelector('.arc-hero-media');
            if (!img) { return; }
            gsap.fromTo(img,
                { scale: 1 },
                { scale: 1.07, duration: INTERVAL / 1000 + 1.6, ease: 'none',
                  transformOrigin: '50% 50%', overwrite: true });
        }
        kenBurns(slides[0]);

        function goTo(destino) {
            var total = slides.length;
            var siguiente = ((destino % total) + total) % total;   // envuelve en ambos sentidos
            if (busy || siguiente === current) { return; }
            busy = true;
            var out = slides[current];
            var inn = slides[siguiente];
            var outPanel = out.querySelector('.arc-hero-panel');
            var inPanel = inn.querySelector('.arc-hero-panel');

            if (quieto) {
                // Cambio seco: quien pide movimiento reducido no quiere fundidos,
                // pero sí tiene derecho a leer las tres láminas.
                gsap.set(out, { autoAlpha: 0 });
                gsap.set(inn, { autoAlpha: 1 });
                gsap.set([outPanel, inPanel], { clearProps: 'all' });
                busy = false;
            } else {
                gsap.timeline({ onComplete: function () { busy = false; } })
                    .to(outPanel, { autoAlpha: 0, y: -26, duration: 0.45, ease: 'power2.in' }, 0)
                    .to(out, { autoAlpha: 0, duration: 0.85, ease: 'power1.inOut' }, 0.2)
                    .fromTo(inn, { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.85, ease: 'power1.inOut' }, 0.2)
                    .add(function () { kenBurns(inn); }, 0.2)
                    .fromTo(inPanel,
                        { autoAlpha: 0, y: 30 },
                        { autoAlpha: 1, y: 0, duration: 0.55, ease: 'power2.out' }, 0.6);
            }

            if (countEl) { countEl.textContent = '0' + (siguiente + 1); }
            current = siguiente;
        }

        /* --- Avance automático -------------------------------------------
           setInterval con un intervalo largo se desfasa si la pestaña queda
           en segundo plano: el navegador acumula disparos y al volver saltan
           varias láminas de golpe. Con setTimeout encadenado cada espera
           empieza cuando termina la anterior, y se puede cancelar de verdad
           al pausar —cosa que el setInterval anterior no hacía nunca—. */
        function arranca() {
            if (pausado || timer) { return; }
            timer = window.setTimeout(function () {
                timer = null;
                if (!document.hidden) { goTo(current + 1); }
                arranca();
            }, INTERVAL);
        }

        function detiene() {
            if (timer) { window.clearTimeout(timer); timer = null; }
        }

        // La cinta de logos es el otro movimiento automático de la portada y el
        // mismo botón la manda. Si slick no llegó a montarse no pasa nada: ahí
        // los logos son una fila que se arrastra a mano y no hay qué pausar.
        function logos(orden) {
            if (!window.jQuery || !logosPista) { return; }
            if (!logosPista.classList.contains('slick-initialized')) { return; }
            window.jQuery(logosPista).slick(orden);
        }

        function pausa(valor) {
            pausado = valor;
            if (toggle) { toggle.setAttribute('aria-pressed', valor ? 'true' : 'false'); }
            logos(valor ? 'slickPause' : 'slickPlay');
            if (valor) { detiene(); } else { arranca(); }
        }

        if (toggle) {
            toggle.addEventListener('click', function () { pausa(!pausado); });
            // Con movimiento reducido no hay nada que pausar: el conmutador
            // sobra y se retira del orden de tabulación en vez de mentir.
            if (!automatico) { toggle.hidden = true; }
        }
        // Mover a mano implica tomar el control: se detiene el avance solo, que
        // es lo que espera quien está leyendo una lámina concreta.
        if (prev) { prev.addEventListener('click', function () { pausa(true); goTo(current - 1); }); }
        if (next) { next.addEventListener('click', function () { pausa(true); goTo(current + 1); }); }

        arranca();
    }


    /* ==========================================================================
       11. Barra de progreso de lectura
       ========================================================================== */
    function progressBar() {
        if (document.querySelector('.arc-progress')) { return; }

        var bar = document.createElement('div');
        bar.className = 'arc-progress';
        bar.setAttribute('aria-hidden', 'true');
        document.body.appendChild(bar);

        // Sin elemento disparador: el template fija `html, body { height: 100% }`
        // (style.css), así que el rectángulo de <html> mide lo que la ventana y un
        // `end: 'bottom bottom'` se resolvería en 0 — la barra no se movería nunca.
        // El recorrido se toma directamente del scroll de la página.
        gsap.to(bar, {
            scaleX: 1,
            ease: 'none',
            scrollTrigger: {
                start: 0,
                end: function () { return ScrollTrigger.maxScroll(window); },
                scrub: 0.2,
                invalidateOnRefresh: true
            }
        });
    }

    /* ==========================================================================
       12. Arranque
       --------------------------------------------------------------------------
       Se espera al `load`, al precargador (main.js lo desvanece a los 500ms) y a
       que las fuentes estén listas —si se parten las líneas de un titular antes
       de que cargue la tipografía, los cortes salen donde no son—. Hasta ese
       momento no se oculta nada: si algo fallara antes, la página se queda
       visible y completa.
       ========================================================================== */
    // Cada módulo va aislado. Si uno fallara —un elemento que desaparece a media
    // construcción, una versión distinta de una librería—, los demás se montan
    // igual y, sobre todo, se llega al refresco y a la red de rescate del final.
    // Sin esto, una excepción a mitad dejaría medio sitio con el estado inicial
    // aplicado y sin nadie que lo revele: contenido invisible.
    function safely(nombre, fn) {
        try {
            fn();
        } catch (err) {
            if (window.console && console.warn) {
                console.warn('[arcondec-motion] ' + nombre + ' no se pudo montar:', err);
            }
        }
    }

    function start() {
        // Va antes que revealRows: marca sus columnas con data-arc-motion="off"
        // para que el sistema genérico no las anime también.
        safely('revealArticleCards', revealArticleCards);
        safely('revealRows', revealRows);
        safely('revealFeatureMedia', revealFeatureMedia);
        safely('revealMap', revealMap);
        safely('revealBanner', revealBanner);
        safely('parallaxBackgrounds', parallaxBackgrounds);
        safely('heroSlides', heroSlides);
        safely('logoCarousel', logoCarousel);
        safely('progressBar', progressBar);

        // Las fotos que terminan de cargar cambian el alto de la página y
        // desplazan los puntos de disparo.
        safely('refresh', function () { ScrollTrigger.refresh(); });

        ScrollTrigger.addEventListener('scrollEnd', function () {
            safely('rescuePending', rescuePending);
        });
    }

    function boot() {
        if (document.fonts && document.fonts.ready && document.fonts.ready.then) {
            document.fonts.ready.then(start, start);
        } else {
            start();
        }
    }

    if (document.readyState === 'complete') {
        window.setTimeout(boot, 100);
    } else {
        window.addEventListener('load', function () { window.setTimeout(boot, 500); });
    }

})(window, document);
