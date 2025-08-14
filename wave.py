
import wavedrom

wave = \
"""
{signal: [
  {name: 'AlarmIn [Sender]', wave: '010........', data:["ALARM_FRAME"]},
  {name: 'AlarmVerarbeitet [Empfänger]', wave: '0........10'},



]}


"""

svg = wavedrom.render(wave)
svg.saveas("x.svg")
