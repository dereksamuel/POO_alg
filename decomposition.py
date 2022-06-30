class HospitalRoom:
  def __init__(self, area, color, type, status, room_movements=None):
    self._area = area
    self.color = color.lower()
    self.type = type
    self.status = status
    self.room_movements = room_movements


class CardiologyRoomUtils:
  def __init__(self, crono_meter_number:int=0):
    self.status_client = {}
    self.crono_meter_number = crono_meter_number

  def taking_pulse(self, pulse_per_minute:int):
    if pulse_per_minute < 15:
      self.status_client["pulse_per_minute"] = "very slow"
      return "You are wrong, your pulse is very low"
    else:
      self.status_client["pulse_per_minute"] = "OK"
      return "You are ok"

if __name__ == "__main__":
  room1 = HospitalRoom(
    area=150,
    color="green",
    type="Cardiology",
    status="is free",
    room_movements=CardiologyRoomUtils()
  )
  print(room1.room_movements.taking_pulse(15))

  print(room1.room_movements.status_client)
