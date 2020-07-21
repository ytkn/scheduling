import React from 'react';
import SelectorScss from "../css/Selector.scss"
import classnames from "classnames"

type Props = {
  choices: string[]
  currentChoice: string
  onChoice: (s: string) => void
}

const Selector: React.FC<Props> = (props: Props) =>
  <div className={SelectorScss['selector']}>
    {props.choices.map(choice =>
      <div
        key={choice}
        className={
          choice === props.currentChoice ?
            classnames([
              SelectorScss['selector__item--selected'],
              SelectorScss['selector__item']
            ]) :
            SelectorScss['selector__item']}
        onClick={() => props.onChoice(choice)}
      >
        {choice}
      </div>
    )}
  </div>

export default Selector