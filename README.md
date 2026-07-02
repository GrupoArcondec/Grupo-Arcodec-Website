<div align="center">

# Grupo Arcondec — Sitio corporativo

**Infraestructura eléctrica industrial y centros de datos · México**

Landing corporativa premium con sistema de diseño editorial propio, animaciones
de alto nivel y contenido 100 % real de la operación de Grupo Arcondec.

</div>

---

## ✨ Características

- **Sistema de diseño editorial propio** (`src/studio.css`, prefijo `st-`): retícula de 4 columnas, contenedor de 1520 px, escala tipográfica estricta por breakpoint y sistema de radios unificado.
- **Identidad de marca oficial**: paleta azules + ámbar (navy `#08182B`, cobalt `#1B3FA0`, electric `#3D6BF5`, ámbar `#FFC20E`, hielo `#CFE3F5`, claro `#EEF1F6`) y logotipo `ARC⏻NDEC` con el símbolo de encendido como componente SVG escalable.
- **Animaciones premium**: intro con máscara de texto, cascada de reveals al hacer scroll con física de resorte, contadores animados, texto que se enciende palabra a palabra, acordeones fluidos, divisores que se dibujan, micro-interacciones en botones (text-roll) y hovers cinematográficos en tarjetas (blur + zoom + semáforo).
- **Scroll suave** con Lenis sincronizado a las animaciones.
- **Responsive real de 3 breakpoints** (desktop ≥ 1200 px · tablet 810–1199 px · móvil ≤ 810 px) con tamaños tipográficos fijos por rango y variantes táctiles de cada interacción.
- **Accesibilidad**: contraste AA verificado en los pares principales, `prefers-reduced-motion`, foco visible y semántica correcta.
- **Contenido verificable**: 16 hubs de proyecto con fotografía real de obra, 7 servicios con alcances, métricas reales (+30 años, 225 kVA–2.5 MVA, 24/7), clientes y blog oficiales. Sin testimonios ni cifras inventadas.
- **Contacto directo**: formulario que abre WhatsApp con el mensaje prellenado (sin backend).

## 🛠 Stack

| Capa | Tecnología |
|---|---|
| Framework | React 18 + TypeScript |
| Bundler | Vite 5 |
| Estilos | CSS moderno con design tokens propios (`studio.css`) + Tailwind CSS (tokens de marca) |
| Animación | CSS transitions/keyframes + scroll-driven animations, Lenis (smooth scroll), GSAP + ScrollTrigger (módulos internos) |
| 3D / vectorial | Three.js (mapa de cobertura), Lottie |
| Ruteo | React Router 6 |
| Tipografía | Inter (Google Fonts) |

## 📁 Estructura

```
arcondec-studio/
├── public/
│   └── brand/               # Activos oficiales de marca (logo)
├── src/
│   ├── components/
│   │   ├── studio/          # Sistema de diseño de la home (Hero, Proyectos,
│   │   │                    #   Servicios, Experiencias, Cotiza, FAQ, Blog, Contacto…)
│   │   ├── Nav.tsx          # Navegación + menú desplegable
│   │   └── …                # Componentes de subpáginas (blog, servicios, carreras)
│   ├── hooks/               # useLenis (scroll suave), useInView
│   ├── lib/data.ts          # Única fuente de contenido (servicios, hubs, clientes, blog)
│   ├── studio.css           # Design system de la home (tokens --st-*)
│   └── index.css            # Estilos de subpáginas
├── tailwind.config.js       # Paleta oficial de marca
└── vite.config.ts
```

## 🚀 Desarrollo

Requisitos: **Node 18+**.

```bash
npm install
npm run dev -- --port 5180   # entorno local en http://localhost:5180
npm run build                # type-check + build de producción (dist/)
npm run preview              # sirve el build localmente
```

El build es 100 % estático (`base: './'`): puede desplegarse en cualquier
hosting estático (Vercel, Netlify, S3, Hostinger…).

Los assets fotográficos y logos de clientes se cargan del dominio oficial
**arcondec.mx**; el punto único de origen es `ASSET` en `src/lib/data.ts`.
Para empaquetarlos localmente: copia la carpeta `/assets` del servidor a
`public/` y cambia `ASSET` a `''`.

## 🎨 Identidad y personalización

- **Colores / tokens**: `tailwind.config.js` (canon de marca) y `:root` de `src/studio.css`.
- **Logotipo**: componente `LogoArcondec` (`src/components/studio/ui.tsx`) — wordmark tipográfico con el símbolo de encendido en ámbar como SVG que escala con el texto (variantes para fondo claro y oscuro). Originales en `public/brand/`.
- **Contenido** (servicios, hubs, clientes, blog, cobertura): arrays en `src/lib/data.ts`.

## 📄 Licencia

Software propietario. **© 2026 SAM VG. Todos los derechos reservados.**
Desarrollado por **JectCode**. Ver [`LICENSE`](./LICENSE).

Queda prohibida la reproducción, distribución o modificación total o parcial
de este software sin autorización expresa y por escrito del titular.
