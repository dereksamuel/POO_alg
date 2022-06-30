import time


class Nevera:
  def __init__(self, temperature):
    self.temperature = temperature
    pass


  def _start_cronometer(self, crono_end:int, crono_start:int=0):
    while crono_start < crono_end:
      time.sleep(1)
      crono_start += 1
      self._temperature_up(crono_end * 10)
    print("Refrigeration completed")


  def _temperature_up(self, level):
    self.temperature = level

    if level > 250:
      print("nevera temperatures it's hot")
    else:
      print("nevera temperatures it's cold")

  def refrigeration(self, duration):
    self._start_cronometer(crono_start=0, crono_end=duration)


if __name__ == "__main__":
  nevera = Nevera(temperature=250)
  nevera.refrigeration(duration=int(input("How long is you refigeretion time?")))
