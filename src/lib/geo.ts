import raw from './mx_states.json'

export interface MxState {
  n: string
  id: string | number
  p: number[][][]
}

export const MX_STATES = raw as unknown as MxState[]
