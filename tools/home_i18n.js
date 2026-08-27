/*
 * i18n ES/EN — Grupo Arcondec
 * Copy ES: https://arcondec.mx/  ·  Copy EN: https://arcondec.mx/EN/Default.aspx
 * Un solo HTML: los textos marcados con [data-i18n] se intercambian sin recargar.
 * Los enlaces con [data-href-en] cambian a su URL equivalente en inglés.
 */
(function () {
    'use strict';

    var I18N = {
        es: {
            pageTitle: 'Grupo Arcondec — Infraestructura Eléctrica y Data Centers',
            metaDesc: 'Infraestructura eléctrica industrial y data centers en México: más de 30 años en proyectos llave en mano, de la etapa conceptual a la entrega final.',

            topSalesMail: 'ventas@arcondec.mx',
            topLogin: 'Iniciar sesión',

            navAbout: 'Sobre nosotros',
            navProjects: 'Proyectos',
            navServices: 'Servicios',
            navSrvProye: 'Proyectos eléctricos',
            navSrvEstel: 'Estudios eléctricos',
            navSrvCorac: 'Corriente directa (DC)',
            navSrvGespr: 'Gestión de proyectos',
            navSrvCosdc: 'Construcción llave en mano',
            navSrvCivdc: 'Ingeniería civil',
            navSrvIngdc: 'Servicios de Ingeniería',
            navWork: 'Trabaja con nosotros',
            navBlogs: 'Blogs',
            navContact: 'Contáctanos',
            navContactBtn: 'Contáctanos',

            heroBrand: 'GRUPO ARCONDEC',
            heroBtn: 'Habla con un asesor',
            heroMore: 'Conoce más',
            heroS1Title: 'Diseño y Construcción de Data Centers',
            heroS1Text: 'Desarrollamos Data Centers de misión crítica, integrando ingeniería, construcción y equipamiento especializado para garantizar seguridad, eficiencia y continuidad operativa en cada proyecto.',
            heroS2Title: 'Infraestructura Crítica y Energía Ininterrumpida',
            heroS2Text: 'Diseñamos e implementamos infraestructura eléctrica, sistemas UPS, plantas de emergencia y soluciones de respaldo que aseguran la disponibilidad y confiabilidad de operaciones críticas.',
            heroS3Title: 'Operación y Mantenimiento de Infraestructura Crítica',
            heroS3Text: 'Acompañamos a nuestros clientes durante todo el ciclo de vida de su infraestructura mediante servicios especializados de operación, mantenimiento preventivo y correctivo, optimización y atención de emergencias para garantizar la máxima disponibilidad de sus instalaciones.',

            // Controles del hero. Van dentro de cada botón en un <span class="sr-only">:
            // no se ven, pero son el nombre accesible del botón. El estado
            // pausado/en marcha lo comunica aria-pressed, así que el rótulo no cambia.
            heroPrev: 'Lámina anterior',
            heroNext: 'Lámina siguiente',
            heroPause: 'Pausar la rotación automática',

            // Franja de certificaciones ISO bajo el hero. Claves propias: las de
            // sec1/sec2/map se reutilizan más abajo en la página y no se pueden tocar.
            isoQTitle: 'ISO 9001: Calidad',
            isoQText: 'Procesos eficientes y mejora continua.',
            isoETitle: 'ISO 14001: Medio Ambiente',
            isoEText: 'Operaciones responsables con el entorno.',
            isoSTitle: 'ISO 45001: Seguridad y Salud',
            isoSText: 'Prevención de riesgos laborales.',


            dunsLabel: 'Certificación Dun & Bradstreet',
            navServices2: 'Servicios',
            aboutDunsText: 'Contamos con una certificación financiera.',
            svcIntro: 'Ingeniería eléctrica y centros de datos, desde etapa conceptual hasta entrega final.',
            hub1Name: 'Monterrey · Oficinas centrales',
            hub2Name: 'Ciudad de México · Matriz',
            hub3Name: 'Hub Delicias',
            hub4Name: 'Hub Isla Mujeres',
            hubsLine: 'Hubs en Mexicali, Querétaro, Monterrey, Apodaca, Valle Oriente, Delicias, Toluca, Isla Mujeres y Ciudad de México.',
            commitTitle: 'Fortalecemos cada día nuestro compromiso contigo',
            newsTitle: 'Suscríbete a nuestro boletín para recibir novedades',
            newsPlaceholder: 'Escribe tu correo…',
            newsBtn: 'Únete',

            aboutTitle: 'Grupo Arcondec: Empresa 100% mexicana con más de 30 años de experiencia.',
            aboutText: 'Estamos conformados por un equipo multidisciplinario altamente capacitado lo que nos convierte en especialistas en proyectos de misión crítica y data centers.',
            navAbout2: 'Sobre nosotros',
            aboutYears: 'Años de experiencia',

            mapTitle: 'Cobertura Nacional de Infraestructura',
            mapBtn: 'Agenda tu consulta',

            clientsTitle: 'Nuestros clientes',

            // Sección de blog del inicio: 3 artículos destacados de tools/pages.py
            // (ARTICLES). Si allá se cambian los textos, hay que reflejarlos aquí
            // también — el inicio no lee ese archivo, lleva sus propias claves.
            blogTitle: 'Ideas sobre infraestructura crítica',
            blogIntro: 'Artículos sobre energía, data centers y las decisiones de ingeniería detrás de la alta disponibilidad.',
            blogSoon: 'Próximamente',
            blogP1T: 'Energía crítica en data centers',
            blogP1D: 'El suministro eléctrico indispensable para sistemas que no pueden fallar: UPS, plantas de emergencia, bancos de baterías y distribución de alta confiabilidad.',
            blogP2T: 'Sistemas de alimentación en 400 volts de corriente directa',
            blogP2D: 'Distribución en DC a 400 V: alimenta los equipos de TI directamente, reduce pérdidas por conversión y mejora la eficiencia del sistema.',
            blogP3T: 'La corriente directa que impulsa a los líderes en infraestructura crítica',
            blogP3D: 'La mayoría de los equipos ya operan internamente en DC: mantener la energía en ese formato reduce pérdidas, conversiones y puntos de falla.',


            commitText: 'Fortalecemos cada día nuestro compromiso contigo, brindando un servicio excepcional como tu aliado estratégico en ingeniería eléctrica y centros de datos.',

            // Carrusel de servicios del inicio: dos servicios, con sus componentes
            // como tarjetas. Reemplaza las claves ie1-ie7 / dc1-dc6 anteriores.
            svcCatDC: 'Diseño y Construcción de Data Center',
            svcDC1: 'Ingeniería & Proyecto Ejecutivo',
            svcDC2: 'Obra Civil & Estructura',
            svcDC3: 'Infraestructura eléctrica crítica',
            svcDC4: 'Instalación MEP y especiales',
            svcDC5: 'Sistemas de soporte y seguridad',
            svcCatEE: 'Ingeniería eléctrica de alta disponibilidad',
            svcEE1: 'Soluciones eléctricas para data centers',
            svcEE2: 'Corriente directa (DC)',
            svcEE3: 'Corriente alterna (AC)',
            svcEE4: 'Diseño de Tierras',
            svcEE5: 'Mantenimiento preventivo y correctivo',



            footSalesMail: ' ventas@arcondec.mx',
            footCompany: 'Compañía',
            footAbout: 'Sobre nosotros',
            footProjects: 'Proyectos',
            footWork: 'Trabaja con nosotros',
            footBlogs: 'Blogs',
            footContact: 'Contáctanos',
            footIETitle: 'Ingeniería eléctrica',
            footSrvProye: 'Proyectos eléctricos',
            footSrvEstel: 'Estudios eléctricos',
            footSrvCorac: 'Corriente directa (DC)',
            footSrvGespr: 'Gestión de proyectos',
            footDCTitle: 'Centro de datos',
            footSrvCosdc: 'Construcción llave en mano',
            footSrvCivdc: 'Ingeniería civil',
            footSrvIngdc: 'Servicios de Ingeniería',
            footLinksTitle: 'Enlaces',
            footPrivacy: 'Aviso de privacidad',
            footPrivacy2: 'Aviso de privacidad',
            footLogin: 'Iniciar sesión',
            footCopy: 'Grupo Arcondec S.A. de C.V. Copyright © 2026 | Todos los derechos Reservados'
        },

        en: {
            pageTitle: 'Grupo Arcondec — Electrical Infrastructure and Data Centers',
            metaDesc: 'Grupo Arcondec — Industrial electrical infrastructure and data centers in Mexico. Over 30 years of turnkey projects, from conceptual stage to final delivery.',

            topSalesMail: 'sales@arcondec.mx',
            topLogin: 'Login',

            navAbout: 'About Us',
            navProjects: 'Projects',
            navServices: 'Services',
            navSrvProye: 'Electrical Projects',
            navSrvEstel: 'Electrical Studies',
            navSrvCorac: 'Direct Current (DC)',
            navSrvGespr: 'Project Management',
            navSrvCosdc: 'Turnkey Construction',
            navSrvCivdc: 'Civil Engineering',
            navSrvIngdc: 'Engineering Services',
            navWork: 'Work With Us',
            navBlogs: 'Blogs',
            navContact: 'Contact Us',
            navContactBtn: 'Contact Us',

            heroBrand: 'GRUPO ARCONDEC',
            heroBtn: 'Speak with an Advisor',
            heroMore: 'Learn more',
            heroS1Title: 'Data Center Design & Construction',
            heroS1Text: 'We develop mission-critical data centers, integrating engineering, construction and specialized equipment to ensure security, efficiency and operational continuity in every project.',
            heroS2Title: 'Critical Infrastructure & Uninterrupted Power',
            heroS2Text: 'We design and implement electrical infrastructure, UPS systems, emergency plants and backup solutions that ensure the availability and reliability of critical operations.',
            heroS3Title: 'Critical Infrastructure Operation & Maintenance',
            heroS3Text: 'We support our clients throughout the entire lifecycle of their infrastructure with specialized operation, preventive and corrective maintenance, optimization and emergency response services to guarantee maximum availability of their facilities.',

            heroPrev: 'Previous slide',
            heroNext: 'Next slide',
            heroPause: 'Pause the automatic rotation',

            // Franja de certificaciones ISO bajo el hero (ver nota en el bloque ES).
            isoQTitle: 'ISO 9001: Quality',
            isoQText: 'Efficient processes and continuous improvement.',
            isoETitle: 'ISO 14001: Environment',
            isoEText: 'Environmentally responsible operations.',
            isoSTitle: 'ISO 45001: Health and Safety',
            isoSText: 'Occupational risk prevention.',


            dunsLabel: 'Dun & Bradstreet Certification',
            navServices2: 'Services',
            aboutDunsText: 'We hold a financial certification.',
            svcIntro: 'Electrical engineering and data centers, from conceptual stage to final delivery.',
            hub1Name: 'Monterrey · Headquarters',
            hub2Name: 'Mexico City · Main Office',
            hub3Name: 'Delicias Hub',
            hub4Name: 'Isla Mujeres Hub',
            hubsLine: 'Hubs in Mexicali, Querétaro, Monterrey, Apodaca, Valle Oriente, Delicias, Toluca, Isla Mujeres, and Mexico City.',
            commitTitle: 'We strengthen our commitment to you every day',
            newsTitle: 'Subscribe to our newsletter to receive updates',
            newsPlaceholder: 'Enter email…',
            newsBtn: 'Join us',

            aboutTitle: 'Grupo Arcondec: A 100% Mexican company with over 30 years of experience.',
            aboutText: 'We are made up of a highly skilled multidisciplinary team, making us specialists in mission-critical projects and data centers.',
            navAbout2: 'About Us',
            aboutYears: 'Years of Experience',

            mapTitle: 'National Infrastructure Coverage',
            mapBtn: 'Schedule a consultation',

            clientsTitle: 'Our Clients',

            // Sección de blog del inicio (ver nota en el bloque ES).
            blogTitle: 'Insights on critical infrastructure',
            blogIntro: 'Articles on power, data centers and the engineering decisions behind high availability.',
            blogSoon: 'Coming soon',
            blogP1T: 'Critical power in data centers',
            blogP1D: 'The electrical supply that mission-critical systems cannot do without: UPS, emergency plants, battery banks and high-reliability distribution.',
            blogP2T: '400 volt direct current power systems',
            blogP2D: '400 V DC distribution powers IT equipment directly, cutting conversion losses and improving overall system efficiency.',
            blogP3T: 'The direct current powering leaders in critical infrastructure',
            blogP3D: 'Most equipment already runs internally on DC: keeping power in that format reduces losses, conversions and points of failure.',


            commitText: 'We strengthen our commitment to you every day by delivering exceptional service as your strategic partner in electrical engineering and data centers.',

            // Carrusel de servicios del inicio (ver nota en el bloque ES).
            svcCatDC: 'Data Center Design and Construction',
            svcDC1: 'Engineering & Detailed Design',
            svcDC2: 'Civil Works & Structure',
            svcDC3: 'Critical Electrical Infrastructure',
            svcDC4: 'MEP and Specialty Installation',
            svcDC5: 'Support and Safety Systems',
            svcCatEE: 'High-Availability Electrical Engineering',
            svcEE1: 'Electrical Solutions for Data Centers',
            svcEE2: 'Direct Current (DC)',
            svcEE3: 'Alternating Current (AC)',
            svcEE4: 'Grounding Design',
            svcEE5: 'Preventive and Corrective Maintenance',



            footSalesMail: ' sales@arcondec.mx',
            footCompany: 'Company',
            footAbout: 'About Us',
            footProjects: 'Projects',
            footWork: 'Work With Us',
            footBlogs: 'Blogs',
            footContact: 'Contact Us',
            footIETitle: 'Electrical Engineering',
            footSrvProye: 'Electrical Projects',
            footSrvEstel: 'Electrical Studies',
            footSrvCorac: 'Direct Current (DC)',
            footSrvGespr: 'Project Management',
            footDCTitle: 'Data Center',
            footSrvCosdc: 'Turnkey Construction',
            footSrvCivdc: 'Civil Engineering',
            footSrvIngdc: 'Engineering Services',
            footLinksTitle: 'Links',
            footPrivacy: 'Privacy Notice',
            footPrivacy2: 'Privacy Notice',
            footLogin: 'Login',
            footCopy: 'Grupo Arcondec S.A. de C.V. Copyright © 2026 | All rights reserved'
        }
    };

    var STORAGE_KEY = 'arcondec-lang';

    function applyLang(lang) {
        if (!I18N[lang]) { lang = 'es'; }
        var dict = I18N[lang];

        document.documentElement.setAttribute('lang', lang);
        document.title = dict.pageTitle;
        var meta = document.querySelector('meta[name="description"]');
        if (meta) { meta.setAttribute('content', dict.metaDesc); }

        // Textos
        var nodes = document.querySelectorAll('[data-i18n]');
        for (var i = 0; i < nodes.length; i++) {
            var key = nodes[i].getAttribute('data-i18n');
            if (dict[key] !== undefined) { nodes[i].textContent = dict[key]; }
        }

        // Placeholders de formularios
        var phs = document.querySelectorAll('[data-i18n-placeholder]');
        for (var p = 0; p < phs.length; p++) {
            var pkey = phs[p].getAttribute('data-i18n-placeholder');
            if (dict[pkey] !== undefined) { phs[p].setAttribute('placeholder', dict[pkey]); }
        }

        // Enlaces con equivalente en inglés
        var links = document.querySelectorAll('[data-href-en]');
        for (var j = 0; j < links.length; j++) {
            var el = links[j];
            if (!el.getAttribute('data-href-es')) {
                el.setAttribute('data-href-es', el.getAttribute('href'));
            }
            el.setAttribute('href', lang === 'en' ? el.getAttribute('data-href-en') : el.getAttribute('data-href-es'));
        }

        // Estado del selector ESP | EN
        var switches = document.querySelectorAll('.lang-switch');
        for (var k = 0; k < switches.length; k++) {
            switches[k].classList.toggle('active', switches[k].getAttribute('data-lang') === lang);
        }

        try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) { /* modo privado */ }
    }

    function init() {
        var saved = 'es';
        try { saved = localStorage.getItem(STORAGE_KEY) || 'es'; } catch (e) { /* modo privado */ }

        var switches = document.querySelectorAll('.lang-switch');
        for (var i = 0; i < switches.length; i++) {
            switches[i].addEventListener('click', function (ev) {
                ev.preventDefault();
                applyLang(this.getAttribute('data-lang'));
            });
        }

        applyLang(saved);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
