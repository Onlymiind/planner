export type TimeWindow = { date: string; startTime: string; endTime: string; };
export type PlanRequest = {
  window: TimeWindow;
  slotMinutes: number;
  parallelLimit: number;
  options?: Record<string, any>;
};
export type Slot = {
  start: string; end: string; courtId: string; groupId: string;
  item?: string; judge?: string; comment?: string;
};
export type PlanResponse = { id: string; date: string; slots: Slot[]; };
