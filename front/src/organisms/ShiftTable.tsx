import React, { useState } from 'react';
import { Instance, ShiftRequest, SectionScover } from "../types/instance"
import ShiftTablsScss from "../css/ShiftTable.scss"
import Legend from '../molecules/Legend';
import Balloon from '../atoms/Balloon';

type Props = {
  instance: Instance,
  solution: number[][][]
}

const ShiftTable: React.FC<Props> = ({ instance, solution }: Props) => {

  const [emphasizeViolation, setEmphasizeViolation] = useState(false)

  const days = Array.from(Array(instance.days).keys())

  const shiftString = (x: number[]): string => {
    const list = x.map((y, idx) => y === 1 ? instance.shifts[idx].id : '-').filter(s => s != '-')
    return list.length === 0 ? "-" : list[0]
  }

  const staffId = (staffIdx: number): string => instance.staffs[staffIdx].id

  const hasOffRequest = (day: number, staffIdx: number): boolean =>
    instance.off_requests.filter(offRequest => offRequest.day === day && offRequest.staff_id === staffId(staffIdx)).length > 0

  const hasOnRequest = (day: number, staffIdx: number): boolean =>
    instance.on_requests.filter(onRequest => onRequest.day === day && onRequest.staff_id === staffId(staffIdx)).length > 0

  const getOnRequest = (day: number, staffIdx: number): ShiftRequest =>
    instance.on_requests.filter(onRequest => onRequest.day === day && onRequest.staff_id === staffId(staffIdx))[0]

  const getOffRequest = (day: number, staffIdx: number): ShiftRequest =>
    instance.off_requests.filter(offRequest => offRequest.day === day && offRequest.staff_id === staffId(staffIdx))[0]

  const isDayWeekend = (day: number): boolean => day % 7 == 5 || day % 7 == 6

  const isDayOff = (day: number, staffIdx: number): boolean =>
    instance.days_off.filter(dayOff => dayOff.day === day && dayOff.staff_id === staffId(staffIdx)).length > 0

  const cellStyle = (day: number, staffIdx: number): string => {
    if (isDayOff(day, staffIdx)) return ShiftTablsScss['shiftTable__cell--yellow']
    if (hasOffRequest(day, staffIdx)) return ShiftTablsScss['shiftTable__cell--pink']
    if (hasOnRequest(day, staffIdx)) return ShiftTablsScss['shiftTable__cell--lightgreen']
    if (isDayWeekend(day)) return ShiftTablsScss['shiftTable__cell--lightblue']
    return undefined
  }

  const totalMinutes = (staffIdx: number): number => {
    let sum = 0
    days.forEach(day => {
      instance.shifts.forEach((shift, shiftIdx) => {
        sum += shift.length * solution[day][staffIdx][shiftIdx]
      })
    })
    return sum
  }

  const sectionCover = (day: number, shiftIdx: number): SectionScover => {
    const list = instance.section_covers.filter(cover => cover.day === day && cover.shift_id === instance.shifts[shiftIdx].id)
    return list.length > 0 ? list[0] : undefined
  }

  const shiftCover = (day: number, shiftIdx: number): number =>
    instance.staffs.map((_, staffIdx) => solution[day][staffIdx][shiftIdx]).reduce((a, b) => a + b)

  const shiftCount = (staffIdx: number, shiftIdx: number): number =>
    days.map(day => solution[day][staffIdx][shiftIdx]).reduce((a, b) => a + b)

  return (
    <div className={ShiftTablsScss['shiftTable']}>
      <table>
        <thead>
          <tr>
            <th></th>
            {days.map(day => <th>{day}</th>)}
            <th>min total minutes</th>
            <th>max total minutes</th>
            <th>total minutes</th>
            {instance.shifts.map(shift =>
              <>
                <th>{`max shifts ${shift.id}`}</th>
                <th>{`shift count ${shift.id}`}</th>
              </>
            )}
          </tr>
        </thead>
        <tbody>
          {instance.staffs.map((staff, staffIdx) =>
            <tr>
              <td>{`staff ${staff.id}`}</td>
              {days.map((day) => {
                const hasViolation =
                  (hasOffRequest(day, staffIdx) && shiftString(solution[day][staffIdx]) === getOffRequest(day, staffIdx).shift_id) ||
                  (hasOnRequest(day, staffIdx) && shiftString(solution[day][staffIdx]) !== getOnRequest(day, staffIdx).shift_id)
                const penalty =
                  hasViolation && ((hasOffRequest(day, staffIdx) && getOffRequest(day, staffIdx).weight) ||
                    (hasOnRequest(day, staffIdx) && getOnRequest(day, staffIdx).weight))
                return (
                  <td
                    className={(hasViolation && emphasizeViolation) ?
                      ShiftTablsScss['shiftTable__cell--red'] :
                      cellStyle(day, staffIdx)}
                  >
                    {`${shiftString(solution[day][staffIdx])}`}
                    {`${hasOnRequest(day, staffIdx) ? '/' + getOnRequest(day, staffIdx).shift_id : ''}`}
                    {`${hasOffRequest(day, staffIdx) ? '/!' + getOffRequest(day, staffIdx).shift_id : ''}`}
                    {penalty &&
                      <div className={ShiftTablsScss['penaltyBox']}>
                        <div className={ShiftTablsScss['penalty']}>
                          <Balloon text={`penalty:${penalty}`} />
                        </div>
                      </div>}
                  </td>)
              })}
              <td>{staff.min_total_minutes}</td>
              <td>{staff.max_total_minutes}</td>
              <td>{totalMinutes(staffIdx)}</td>
              {instance.shifts.map((shift, shiftIdx) =>
                <>
                  <td>{staff.max_shifts[shift.id]}</td>
                  <td>{shiftCount(staffIdx, shiftIdx)}</td>
                </>
              )}
            </tr>
          )}
          {instance.shifts.map((shift, shiftIdx) =>
            <>
              <tr>
                <td>{`requirement ${shift.id}`}</td>
                {days.map(day => {
                  const cover = sectionCover(day, shiftIdx)
                  const hasViolation = cover.requirement !== shiftCover(day, shiftIdx)
                  const penalty =
                    hasViolation && Math.max(
                      (shiftCover(day, shiftIdx) - cover.requirement) * cover.weight_for_over,
                      (cover.requirement - shiftCover(day, shiftIdx)) * cover.weight_for_under)
                  return (
                    <td className={hasViolation && emphasizeViolation && ShiftTablsScss['shiftTable__cell--red']}>
                      {cover.requirement}
                      {penalty &&
                        <div className={ShiftTablsScss['penaltyBox']}>
                          <div className={ShiftTablsScss['penalty']}>
                            <Balloon text={`penalty:${penalty}`} />
                          </div>
                        </div>}
                    </td>)
                })}
              </tr>
              <tr>
                <td>{`covers ${shift.id}`}</td>
                {days.map(day => {
                  const cover = sectionCover(day, shiftIdx)
                  const hasViolation = cover.requirement !== shiftCover(day, shiftIdx)
                  const penalty =
                    hasViolation && Math.max(
                      (shiftCover(day, shiftIdx) - cover.requirement) * cover.weight_for_over,
                      (cover.requirement - shiftCover(day, shiftIdx)) * cover.weight_for_under)
                  return (
                    <td className={hasViolation && emphasizeViolation && ShiftTablsScss['shiftTable__cell--red']}>
                      {shiftCover(day, shiftIdx)}
                      {penalty &&
                        <div className={ShiftTablsScss['penaltyBox']}>
                          <div className={ShiftTablsScss['penalty']}>
                            <Balloon text={`penalty:${penalty}`} />
                          </div>
                        </div>}
                    </td>)
                })}
              </tr>
            </>
          )}
        </tbody>
      </table>
      <Legend color='yellow' label='day off' />
      <Legend color='pink' label='off request' />
      <Legend color='lightgreen' label='on request' />
      <Legend color='lightblue' label='weekend' />
      <Legend color='red' label='violation' />
      <input
        type="checkbox" checked={emphasizeViolation}
        onChange={() => setEmphasizeViolation(!emphasizeViolation)} />show violation
    </div >)
}

export default ShiftTable 