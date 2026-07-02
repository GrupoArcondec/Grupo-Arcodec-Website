import { Reveal } from './Button'
import { CLIENTS, img } from '../lib/data'

export function Clients() {
  const row = (arr: typeof CLIENTS) =>
    arr.concat(arr).map((c, i) => (
      <span className="mq-item" key={c.f + i}>
        <img src={img(`clients/${c.f}.png`)} alt={c.n} loading="lazy" />
      </span>
    ))

  return (
    <div className="clients">
      <Reveal><div className="lab">Confían en Grupo Arcondec</div></Reveal>
      <div className="marquee">{row(CLIENTS)}</div>
      <div className="marquee rev">{row([...CLIENTS].reverse())}</div>
    </div>
  )
}
