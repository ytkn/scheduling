import React from 'react';
import ShiftTable from '../organisms/ShiftTable';
import { instance, solution } from "../types/instance"

const ShiftPage: React.FC = () =>
  <div>
    <h1>shift</h1>
    <ShiftTable instance={instance} solution={solution} />
  </div>


export default ShiftPage