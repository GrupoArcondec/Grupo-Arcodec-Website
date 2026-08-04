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
 * - Con `prefers-reduced-motion: reduce` no registra ninguna animación —ni la
 *   suya ni la del template— y la página se queda quieta y completa.
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
       main.js arranca WOW y las animaciones del hero dentro de su
       `jQuery(document).on('ready')`, y este archivo se ejecuta antes (va al final
       del <body>, DOMContentLoaded todavía no ha ocurrido). Al quitar aquí la
       clase `wow` y el atributo `data-animation`, main.js no encuentra a quién
       animar: un solo sistema en la página, sin nada moviéndose dos veces.
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

        var heroNodes = document.querySelectorAll('.hero-slider [data-animation]');
        for (i = 0; i < heroNodes.length; i++) {
            for (j = 0; j < WOW_CLASSES.length; j++) {
                heroNodes[i].classList.remove(WOW_CLASSES[j]);
            }
            heroNodes[i].removeAttribute('data-animation');
            heroNodes[i].removeAttribute('data-delay');
        }
    }

    unhookTemplateMotion();

    // Con animaciones reducidas la página se queda quieta: el template ya no
    // anima nada y aquí no se registra nada más.
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) { return; }

    /* ==========================================================================
       2. Ajustes
       ========================================================================== */
    var SKIP = [
        'header',                 // cabecera y menú: los mueve main.js
        '.preloader',
        '.hero-slider',           // el hero tiene su propia línea de tiempo
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
                if (isColumn(row.children[k]) && isVisible(row.children[k])) {
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
            if (bg.closest('.hero-slider')) { continue; }

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

    /* ==========================================================================
       9. Hero: una línea de tiempo por diapositiva
       --------------------------------------------------------------------------
       Sustituye a las clases de animate.css que aplicaba main.js (barrían el
       titular 700px de lado). Aquí el titular se arma línea a línea y el resto
       entra detrás, con la foto haciendo un zoom lento de fondo. El recorte del
       zoom lo hace el overflow del propio .slick-list.
       ========================================================================== */
    function heroMotion() {
        var jq = window.jQuery;
        var slider = document.querySelector('.hero-slider');
        if (!jq || !slider || !slider.classList.contains('slick-initialized')) { return; }

        var slides = slider.querySelectorAll('.hero-area');
        if (!slides.length) { return; }

        var current = null;

        function play(index) {
            var slide = slides[index];
            if (!slide) { return; }

            var content = slide.querySelector('.hero-2-content');
            var background = slide.querySelector('.section__bg');

            if (background) {
                gsap.fromTo(background, { scale: 1 }, { scale: 1.075, duration: 11, ease: 'none', overwrite: true });
            }
            if (!content) { return; }

            if (current) { revertSplit(current.split); current.tl.kill(); }

            var badge = content.querySelector('span');
            var heading = content.querySelector('.title');
            var text = content.querySelector('.text');
            var buttons = content.querySelectorAll('ul li');
            var playButton = slide.querySelector('.hero-play-11 a');

            var split = heading ? splitLines(heading) : null;
            var tl = gsap.timeline({
                defaults: { ease: EASE },
                onComplete: function () { revertSplit(split); }
            });

            if (badge) { tl.from(badge, { y: -18, opacity: 0, duration: 0.6, clearProps: 'transform,opacity' }, 0); }

            if (split && split.lines.length) {
                tl.from(split.lines, { yPercent: 115, duration: 0.95, stagger: 0.09 }, 0.15);
            } else if (heading) {
                tl.from(heading, { y: 40, opacity: 0, duration: 0.9, clearProps: 'transform,opacity' }, 0.15);
            }

            if (text) { tl.from(text, { y: 24, opacity: 0, duration: 0.7, clearProps: 'transform,opacity' }, 0.5); }
            if (buttons.length) {
                tl.from(buttons, { y: 22, opacity: 0, duration: 0.6, stagger: 0.1, clearProps: 'transform,opacity' }, 0.62);
            }
            if (playButton) {
                tl.from(playButton, { scale: 0.7, opacity: 0, duration: 0.7, ease: 'back.out(1.7)', clearProps: 'transform,opacity' }, 0.5);
            }

            current = { tl: tl, split: split };
        }

        play(jq(slider).slick('slickCurrentSlide') || 0);
        jq(slider).on('beforeChange', function (event, slick, from, to) { play(to); });
    }

    /* ==========================================================================
       10. Logos de clientes: cinta continua, solo en móvil
       --------------------------------------------------------------------------
       En escritorio los diez logos caben en dos líneas de cinco y no se toca nada.
       Al envolverse, en el móvil caían de uno en uno y la sección medía 1078px.
       arcondec.css ya los deja en una tira que se arrastra con el dedo —eso
       funciona sin JavaScript y es lo que ve quien pide movimiento reducido—; aquí
       esa tira pasa a moverse sola, cada línea hacia un lado.

       gsap.matchMedia() se encarga de montar y desmontar según el ancho: al pasar
       a escritorio revierte la animación y la función de limpieza deshace los
       clones, así que el marcado vuelve a quedar como estaba.
       ========================================================================== */
    var MARQUEE_QUERY = '(max-width: 767.98px)';
    var MARQUEE_SPEED = 34;   // píxeles por segundo

    function logoMarquee() {
        var strips = document.querySelectorAll('.brand-3-area .brand-3-items');
        if (!strips.length || !window.matchMedia) { return; }

        var consulta = window.matchMedia(MARQUEE_QUERY);
        var tweens = [];
        var montada = false;

        function montar() {
            Array.prototype.forEach.call(strips, function (strip, index) {
                var originals = Array.prototype.slice.call(strip.children);
                if (originals.length < 2) { return; }

                var track = document.createElement('div');
                track.className = 'arc-marquee-track';

                originals.forEach(function (item) { track.appendChild(item); });

                // Se duplica el juego entero: al desplazar la cinta justo la mitad
                // de su ancho, la copia cae exactamente donde estaba el original y
                // el ciclo no tiene costura. La copia se oculta a los lectores de
                // pantalla y sus enlaces salen del orden de tabulación: es un
                // duplicado visual, no contenido nuevo.
                originals.forEach(function (item) {
                    var copy = item.cloneNode(true);
                    copy.setAttribute('aria-hidden', 'true');
                    Array.prototype.forEach.call(copy.querySelectorAll('a'), function (link) {
                        link.setAttribute('tabindex', '-1');
                    });
                    track.appendChild(copy);
                });

                strip.appendChild(track);
                strip.classList.add('arc-marquee');

                var recorrido = track.scrollWidth / 2;
                if (recorrido < 1) { return; }

                // Misma velocidad en las dos líneas aunque midan distinto, y en
                // sentidos opuestos: se lee como una sola pieza en movimiento.
                var haciaAtras = index % 2 === 1;
                var tween = gsap.fromTo(track,
                    { xPercent: haciaAtras ? -50 : 0 },
                    {
                        xPercent: haciaAtras ? 0 : -50,
                        duration: recorrido / MARQUEE_SPEED,
                        ease: 'none',
                        repeat: -1
                    }
                );
                tweens.push(tween);

                // Al posar el dedo se detiene, para poder mirar un logo concreto.
                strip.addEventListener('pointerenter', function () { tween.pause(); });
                strip.addEventListener('pointerleave', function () { tween.resume(); });
            });

            // La tira cambia de alto al montarse: los puntos de disparo del resto
            // de la página se recalculan.
            scheduleRefresh();
        }

        function desmontar() {
            tweens.forEach(function (t) { t.kill(); });
            tweens = [];

            Array.prototype.forEach.call(strips, function (strip) {
                var track = strip.querySelector('.arc-marquee-track');
                if (!track) { return; }
                Array.prototype.slice.call(track.children).forEach(function (node) {
                    if (node.getAttribute('aria-hidden') === 'true') {
                        node.parentNode.removeChild(node);
                    } else {
                        strip.appendChild(node);
                    }
                });
                track.parentNode.removeChild(track);
                strip.classList.remove('arc-marquee');
            });

            scheduleRefresh();
        }

        // El montaje y el desmontaje van con listener propio en vez de delegarlos
        // a gsap.matchMedia(): dejar un juego de clones colgado al pasar a
        // escritorio deja la sección en 1271px —peor que el problema que
        // resolvemos—, así que conviene que sea explícito y comprobable. El
        // `resize` es la red por si el evento `change` no llega.
        function sincroniza() {
            if (consulta.matches === montada) { return; }
            montada = consulta.matches;
            if (montada) { montar(); } else { desmontar(); }
        }

        sincroniza();

        if (consulta.addEventListener) {
            consulta.addEventListener('change', sincroniza);
        } else if (consulta.addListener) {
            consulta.addListener(sincroniza);
        }
        window.addEventListener('resize', sincroniza);
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
        safely('revealRows', revealRows);
        safely('revealFeatureMedia', revealFeatureMedia);
        safely('revealBanner', revealBanner);
        safely('parallaxBackgrounds', parallaxBackgrounds);
        safely('heroMotion', heroMotion);
        safely('logoMarquee', logoMarquee);
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
