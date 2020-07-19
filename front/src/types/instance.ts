export type Instance = {
  days: number,
  shifts: Shift[],
  staffs: Staff[],
  days_off: DayOff[],
  on_requests: ShiftRequest[],
  off_requests: ShiftRequest[],
  section_covers: SectionScover[]
}

type Shift = {
  id: string,
  length: number,
  forbidden: string[],

}

type Staff = {
  id: string,
  max_shifts: object,
  max_total_minutes: number,
  min_total_minutes: number,
  max_consecutive_shifts: number,
  min_consecutive_shifts: number,
  min_consecutive_days_off: number,
  max_weekends: number
}

type DayOff = {
  staff_id: string,
  day: number
}

export type ShiftRequest = {
  staff_id: string,
  day: number,
  shift_id: string,
  weight: number
}

export type SectionScover = {
  day: number,
  shift_id: string,
  requirement: number,
  weight_for_under: number,
  weight_for_over: number
}

export const instance = {
  days: 14,
  shifts: [
    {
      id: "E",
      length: 480,
      forbidden: [

      ]
    },
    {
      id: "L",
      length: 480,
      forbidden: [
        "E"
      ],
    }
  ],
  staffs: [
    {
      id: "A",
      max_shifts: {
        "E": 14,
        "L": 14
      },
      max_total_minutes: 4320,
      min_total_minutes: 3360,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 2,
      min_consecutive_days_off: 2,
      max_weekends: 1
    },
    {
      id: "B",
      max_shifts: {
        "E": 14,
        "L": 14
      },
      max_total_minutes: 4320,
      min_total_minutes: 3360,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 2,
      min_consecutive_days_off: 2,
      max_weekends: 1
    },
    {
      id: "C",
      max_shifts: {
        "E": 14,
        "L": 14
      },
      max_total_minutes: 4320,
      min_total_minutes: 3360,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 2,
      min_consecutive_days_off: 2,
      max_weekends: 1
    },
    {
      id: "D",
      max_shifts: {
        "E": 14,
        "L": 0
      },
      max_total_minutes: 4320,
      min_total_minutes: 3360,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 2,
      min_consecutive_days_off: 2,
      max_weekends: 1
    },
    {
      id: "E",
      max_shifts: {
        "E": 0,
        "L": 14
      },
      max_total_minutes: 4320,
      min_total_minutes: 3360,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 2,
      min_consecutive_days_off: 2,
      max_weekends: 1
    },
    {
      id: "F",
      max_shifts: {
        "E": 14,
        "L": 14
      },
      max_total_minutes: 4320,
      min_total_minutes: 3360,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 2,
      min_consecutive_days_off: 2,
      max_weekends: 1
    },
    {
      id: "G",
      max_shifts: {
        "E": 14,
        "L": 14
      },
      max_total_minutes: 4320,
      min_total_minutes: 3360,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 2,
      min_consecutive_days_off: 2,
      max_weekends: 1
    },
    {
      id: "H",
      max_shifts: {
        "E": 14,
        "L": 14
      },
      max_total_minutes: 4320,
      min_total_minutes: 3360,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 2,
      min_consecutive_days_off: 2,
      max_weekends: 1
    },
    {
      id: "I",
      max_shifts: {
        "E": 14,
        "L": 14
      },
      max_total_minutes: 4320,
      min_total_minutes: 3360,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 2,
      min_consecutive_days_off: 2,
      max_weekends: 1
    },
    {
      id: "J",
      max_shifts: {
        "E": 14,
        "L": 14
      },
      max_total_minutes: 4320,
      min_total_minutes: 3360,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 2,
      min_consecutive_days_off: 2,
      max_weekends: 1
    },
    {
      id: "K",
      max_shifts: {
        "E": 0,
        "L": 14
      },
      max_total_minutes: 2160,
      min_total_minutes: 1200,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 1,
      min_consecutive_days_off: 1,
      max_weekends: 1
    },
    {
      id: "L",
      max_shifts: {
        "E": 0,
        "L": 14
      },
      max_total_minutes: 2160,
      min_total_minutes: 1200,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 1,
      min_consecutive_days_off: 1,
      max_weekends: 1
    },
    {
      id: "M",
      max_shifts: {
        "E": 14,
        "L": 14
      },
      max_total_minutes: 2160,
      min_total_minutes: 1200,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 1,
      min_consecutive_days_off: 1,
      max_weekends: 1
    },
    {
      id: "N",
      max_shifts: {
        "E": 14,
        "L": 14
      },
      max_total_minutes: 2160,
      min_total_minutes: 1200,
      max_consecutive_shifts: 5,
      min_consecutive_shifts: 1,
      min_consecutive_days_off: 1,
      max_weekends: 1
    }
  ],
  days_off: [
    {
      staff_id: "A",
      day: 3
    },
    {
      staff_id: "B",
      day: 1
    },
    {
      staff_id: "C",
      day: 2
    },
    {
      staff_id: "D",
      day: 12
    },
    {
      staff_id: "E",
      day: 1
    },
    {
      staff_id: "F",
      day: 13
    },
    {
      staff_id: "G",
      day: 9
    },
    {
      staff_id: "H",
      day: 3
    },
    {
      staff_id: "I",
      day: 0
    },
    {
      staff_id: "J",
      day: 8
    },
    {
      staff_id: "K",
      day: 5
    },
    {
      staff_id: "L",
      day: 2
    },
    {
      staff_id: "M",
      day: 8
    },
    {
      staff_id: "N",
      day: 6
    }
  ],
  on_requests: [
    {
      staff_id: "A",
      day: 5,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "A",
      day: 6,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "A",
      day: 7,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "A",
      day: 8,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "A",
      day: 9,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "B",
      day: 7,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "B",
      day: 8,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "B",
      day: 9,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "B",
      day: 10,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "C",
      day: 8,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "C",
      day: 9,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "C",
      day: 10,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "C",
      day: 11,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "D",
      day: 1,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "D",
      day: 2,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "D",
      day: 3,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "E",
      day: 3,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "E",
      day: 4,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "E",
      day: 5,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "E",
      day: 6,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "E",
      day: 7,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "E",
      day: 12,
      shift_id: "L",
      weight: 2
    },
    {
      staff_id: "E",
      day: 13,
      shift_id: "L",
      weight: 2
    },
    {
      staff_id: "F",
      day: 3,
      shift_id: "L",
      weight: 3
    },
    {
      staff_id: "F",
      day: 4,
      shift_id: "L",
      weight: 3
    },
    {
      staff_id: "F",
      day: 5,
      shift_id: "L",
      weight: 3
    },
    {
      staff_id: "I",
      day: 2,
      shift_id: "L",
      weight: 3
    },
    {
      staff_id: "I",
      day: 3,
      shift_id: "L",
      weight: 3
    },
    {
      staff_id: "I",
      day: 12,
      shift_id: "E",
      weight: 2
    },
    {
      staff_id: "J",
      day: 11,
      shift_id: "L",
      weight: 3
    },
    {
      staff_id: "K",
      day: 7,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "K",
      day: 8,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "K",
      day: 9,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "L",
      day: 3,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "L",
      day: 4,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "L",
      day: 10,
      shift_id: "L",
      weight: 3
    },
    {
      staff_id: "L",
      day: 11,
      shift_id: "L",
      weight: 3
    },
    {
      staff_id: "L",
      day: 12,
      shift_id: "L",
      weight: 3
    },
    {
      staff_id: "L",
      day: 13,
      shift_id: "L",
      weight: 3
    },
    {
      staff_id: "M",
      day: 3,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "M",
      day: 4,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "M",
      day: 5,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "M",
      day: 6,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "M",
      day: 7,
      shift_id: "L",
      weight: 1
    },
    {
      staff_id: "N",
      day: 0,
      shift_id: "E",
      weight: 2
    },
    {
      staff_id: "N",
      day: 1,
      shift_id: "E",
      weight: 2
    },
    {
      staff_id: "N",
      day: 2,
      shift_id: "E",
      weight: 2
    },
    {
      staff_id: "N",
      day: 8,
      shift_id: "E",
      weight: 3
    },
    {
      staff_id: "N",
      day: 9,
      shift_id: "E",
      weight: 3
    },
    {
      staff_id: "N",
      day: 10,
      shift_id: "E",
      weight: 3
    }
  ],
  off_requests: [
    {
      staff_id: "G",
      day: 3,
      shift_id: "E",
      weight: 2
    },
    {
      staff_id: "G",
      day: 4,
      shift_id: "E",
      weight: 2
    },
    {
      staff_id: "G",
      day: 5,
      shift_id: "E",
      weight: 2
    },
    {
      staff_id: "G",
      day: 6,
      shift_id: "E",
      weight: 2
    },
    {
      staff_id: "G",
      day: 7,
      shift_id: "E",
      weight: 2
    },
    {
      staff_id: "H",
      day: 1,
      shift_id: "L",
      weight: 2
    },
    {
      staff_id: "J",
      day: 1,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "J",
      day: 2,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "J",
      day: 3,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "J",
      day: 4,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "J",
      day: 5,
      shift_id: "E",
      weight: 1
    },
    {
      staff_id: "M",
      day: 11,
      shift_id: "L",
      weight: 1
    }
  ],
  section_covers: [
    {
      day: 0,
      shift_id: "E",
      requirement: 4,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 0,
      shift_id: "L",
      requirement: 4,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 1,
      shift_id: "E",
      requirement: 4,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 1,
      shift_id: "L",
      requirement: 3,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 2,
      shift_id: "E",
      requirement: 3,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 2,
      shift_id: "L",
      requirement: 6,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 3,
      shift_id: "E",
      requirement: 5,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 3,
      shift_id: "L",
      requirement: 4,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 4,
      shift_id: "E",
      requirement: 3,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 4,
      shift_id: "L",
      requirement: 4,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 5,
      shift_id: "E",
      requirement: 5,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 5,
      shift_id: "L",
      requirement: 5,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 6,
      shift_id: "E",
      requirement: 5,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 6,
      shift_id: "L",
      requirement: 5,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 7,
      shift_id: "E",
      requirement: 3,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 7,
      shift_id: "L",
      requirement: 2,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 8,
      shift_id: "E",
      requirement: 4,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 8,
      shift_id: "L",
      requirement: 4,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 9,
      shift_id: "E",
      requirement: 4,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 9,
      shift_id: "L",
      requirement: 4,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 10,
      shift_id: "E",
      requirement: 4,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 10,
      shift_id: "L",
      requirement: 3,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 11,
      shift_id: "E",
      requirement: 2,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 11,
      shift_id: "L",
      requirement: 3,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 12,
      shift_id: "E",
      requirement: 4,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 12,
      shift_id: "L",
      requirement: 3,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 13,
      shift_id: "E",
      requirement: 3,
      weight_for_under: 100,
      weight_for_over: 1
    },
    {
      day: 13,
      shift_id: "L",
      requirement: 5,
      weight_for_under: 100,
      weight_for_over: 1
    }
  ],
} as Instance


export const solution = [[[1, 0],
[0, 1],
[0, 1],
[1, 0],
[0, 0],
[0, 0],
[1, 0],
[1, 0],
[0, 0],
[0, 1],
[0, 0],
[0, 0],
[0, 1],
[0, 0],],

[[0, 1],
[0, 0],
[0, 0],
[1, 0],
[0, 0],
[0, 0],
[1, 0],
[1, 0],
[1, 0],
[0, 1],
[0, 0],
[0, 1],
[0, 0],
[0, 0],],

[[0, 1],
[0, 0],
[0, 0],
[1, 0],
[0, 1],
[1, 0],
[1, 0],
[0, 1],
[0, 1],
[0, 1],
[0, 1],
[0, 0],
[0, 0],
[0, 0],],

[[0, 0],
[1, 0],
[1, 0],
[1, 0],
[0, 1],
[0, 1],
[1, 0],
[0, 0],
[0, 1],
[0, 1],
[0, 0],
[0, 0],
[1, 0],
[0, 0],],

[[0, 0],
[1, 0],
[1, 0],
[1, 0],
[0, 1],
[0, 1],
[0, 0],
[0, 0],
[0, 1],
[0, 1],
[0, 0],
[0, 0],
[0, 0],
[0, 0],],

[[0, 1],
[0, 0],
[1, 0],
[0, 0],
[0, 1],
[0, 1],
[0, 0],
[1, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 1],
[0, 0],],

[[0, 1],
[0, 0],
[1, 0],
[0, 0],
[0, 1],
[0, 1],
[0, 0],
[1, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 1],
[0, 0],],

[[0, 1],
[1, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 1],
[1, 0],
[1, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],],

[[0, 1],
[1, 0],
[0, 0],
[1, 0],
[0, 0],
[0, 0],
[0, 1],
[0, 1],
[1, 0],
[0, 0],
[0, 1],
[0, 0],
[0, 0],
[1, 0],],

[[0, 1],
[1, 0],
[1, 0],
[1, 0],
[0, 1],
[0, 1],
[0, 0],
[0, 1],
[1, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],],

[[0, 0],
[0, 0],
[1, 0],
[1, 0],
[0, 1],
[0, 1],
[0, 0],
[0, 0],
[0, 0],
[1, 0],
[0, 0],
[0, 1],
[0, 0],
[1, 0],],

[[0, 0],
[0, 0],
[1, 0],
[0, 0],
[0, 1],
[0, 1],
[1, 0],
[0, 0],
[0, 0],
[0, 1],
[0, 0],
[0, 0],
[0, 0],
[0, 0],],

[[0, 0],
[1, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[1, 0],
[0, 0],
[1, 0],
[0, 1],
[0, 1],
[0, 1],
[0, 0],
[1, 0],],

[[0, 0],
[0, 1],
[0, 0],
[1, 0],
[0, 0],
[0, 0],
[1, 0],
[0, 0],
[0, 1],
[0, 1],
[0, 1],
[0, 1],
[0, 0],
[1, 0]]]