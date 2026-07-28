/*
 * Contadores de la pagina de Proyectos.
 *
 * El contador del template (.count en main.js) escribe el numero crudo, y
 * "130000" se lee mal. Este usa su propia clase (.arc-count) para no chocar con
 * el del template y formatea con separador de miles del idioma de la pagina.
 *
 * Sin dependencias: usa IntersectionObserver, y si no existe pinta el valor
 * final directamente (el dato nunca se pierde).
 */
(function () {
    'use strict';

    var DURATION = 2000;

    function format(value, locale) {
        try {
            return value.toLocaleString(locale);
        } catch (err) {
            return String(value);
        }
    }

    function animate(el, locale) {
        var target = parseInt(el.getAttribute('data-count'), 10);
        if (isNaN(target)) { return; }

        var start = null;

        function step(now) {
            if (start === null) { start = now; }
            var progress = Math.min((now - start) / DURATION, 1);
            // easing suave al final, como el 'swing' del template
            var eased = 0.5 - Math.cos(progress * Math.PI) / 2;
            el.textContent = format(Math.round(target * eased), locale);
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        }

        window.requestAnimationFrame(step);
    }

    function init() {
        var nodes = document.querySelectorAll('.arc-count');
        if (!nodes.length) { return; }

        var locale = document.documentElement.getAttribute('lang') === 'en' ? 'en-US' : 'es-MX';

        // Sin soporte de IntersectionObserver o con animaciones reducidas:
        // se muestra el valor final, sin animar.
        var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (!('IntersectionObserver' in window) || reduced) {
            for (var i = 0; i < nodes.length; i++) {
                var value = parseInt(nodes[i].getAttribute('data-count'), 10);
                nodes[i].textContent = isNaN(value) ? '' : format(value, locale);
            }
            return;
        }

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) { return; }
                observer.unobserve(entry.target);
                animate(entry.target, locale);
            });
        }, { threshold: 0.4 });

        for (var j = 0; j < nodes.length; j++) {
            observer.observe(nodes[j]);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
