import React from 'react';
import BalloonScss from "../css/Balloon.scss"

type Props = {
  text: string
}

const Balloon: React.FC<Props> = (props: Props) =>
  <div className={BalloonScss['balloon']}>
    <p>{props.text}</p>
  </div>

export default Balloon