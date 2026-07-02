/* Animación Lottie inline (bodymovin) — pulso eléctrico ámbar/azul.
   Sin assets externos: se pasa como animationData a lottie-web.
   Reemplazable por un .json exportado de After Effects. */
const ring = (
  ind: number,
  color: number[],
  offset: number,
  width: number,
): Record<string, unknown> => ({
  ddd: 0,
  ind,
  ty: 4,
  nm: `ring${ind}`,
  sr: 1,
  ks: {
    o: { a: 1, k: [
      { t: 0 + offset, s: [0] },
      { t: 18 + offset, s: [90] },
      { t: 60 + offset, s: [0] },
    ] },
    r: { a: 0, k: 0 },
    p: { a: 0, k: [100, 100, 0] },
    a: { a: 0, k: [0, 0, 0] },
    s: { a: 1, k: [
      { t: 0 + offset, s: [12, 12, 100] },
      { t: 60 + offset, s: [120, 120, 100] },
    ] },
  },
  shapes: [
    {
      ty: 'gr',
      it: [
        { ty: 'el', d: 1, s: { a: 0, k: [100, 100] }, p: { a: 0, k: [0, 0] } },
        { ty: 'st', c: { a: 0, k: color }, o: { a: 0, k: 100 }, w: { a: 0, k: width }, lc: 2, lj: 1, ml: 4 },
        { ty: 'tr', p: { a: 0, k: [0, 0] }, a: { a: 0, k: [0, 0] }, s: { a: 0, k: [100, 100] }, r: { a: 0, k: 0 }, o: { a: 0, k: 100 } },
      ],
    },
  ],
  ip: 0,
  op: 120,
  st: 0,
  bm: 0,
})

const core: Record<string, unknown> = {
  ddd: 0,
  ind: 9,
  ty: 4,
  nm: 'core',
  sr: 1,
  ks: {
    o: { a: 0, k: 100 },
    r: { a: 0, k: 0 },
    p: { a: 0, k: [100, 100, 0] },
    a: { a: 0, k: [0, 0, 0] },
    s: { a: 1, k: [
      { t: 0, s: [90, 90, 100] },
      { t: 30, s: [110, 110, 100] },
      { t: 60, s: [90, 90, 100] },
    ] },
  },
  shapes: [
    {
      ty: 'gr',
      it: [
        { ty: 'el', d: 1, s: { a: 0, k: [26, 26] }, p: { a: 0, k: [0, 0] } },
        { ty: 'fl', c: { a: 0, k: [1, 0.76, 0.054, 1] }, o: { a: 0, k: 100 } },
        { ty: 'tr', p: { a: 0, k: [0, 0] }, a: { a: 0, k: [0, 0] }, s: { a: 0, k: [100, 100] }, r: { a: 0, k: 0 }, o: { a: 0, k: 100 } },
      ],
    },
  ],
  ip: 0,
  op: 120,
  st: 0,
  bm: 0,
}

const amp = [1, 0.76, 0.054, 1]
const electric = [0.239, 0.419, 0.961, 1]

export const pulseAnimation = {
  v: '5.7.6',
  fr: 60,
  ip: 0,
  op: 120,
  w: 200,
  h: 200,
  nm: 'arcondec-pulse',
  ddd: 0,
  assets: [],
  layers: [
    ring(1, amp, 0, 6),
    ring(2, electric, 20, 4),
    ring(3, amp, 40, 3),
    core,
  ],
}
