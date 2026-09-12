(function () {
    'use strict';
    var grid = document.getElementById('blog-articles');
    var nav = document.querySelector('.arc-blog-pagination');
    if (!grid || !nav) return;
    var items = Array.prototype.slice.call(grid.children);
    var total = Math.ceil(items.length / 6);
    var es = document.documentElement.lang.indexOf('es') === 0;
    var current = 1;
    function render(page, scroll) {
        current = Math.max(1, Math.min(total, page));
        items.forEach(function (item, index) {
            item.hidden = index < (current - 1) * 6 || index >= current * 6;
        });
        nav.replaceChildren();
        function button(label, target, active, disabled) {
            var el = document.createElement('button');
            el.type = 'button';
            el.textContent = label;
            el.disabled = disabled;
            if (active) el.setAttribute('aria-current', 'page');
            el.addEventListener('click', function () { render(target, true); });
            nav.appendChild(el);
        }
        button(es ? 'Anterior' : 'Previous', current - 1, false, current === 1);
        for (var i = 1; i <= total; i++) button(String(i), i, i === current, false);
        button(es ? 'Siguiente' : 'Next', current + 1, false, current === total);
        var status = document.createElement('p');
        status.setAttribute('role', 'status');
        status.textContent = (es ? 'Página ' : 'Page ') + current + (es ? ' de ' : ' of ') + total;
        nav.appendChild(status);
        nav.hidden = total <= 1;
        if (scroll) {
            grid.setAttribute('tabindex', '-1');
            grid.focus({ preventScroll: true });
            grid.scrollIntoView({ behavior: 'auto', block: 'start' });
        }
        if (window.ScrollTrigger) window.ScrollTrigger.refresh();
    }
    render(1, false);
})();
