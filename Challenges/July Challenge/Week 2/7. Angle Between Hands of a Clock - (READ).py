class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hourAngle = (hour+(minutes/60))*30

        hourAngle = (hourAngle-360) if hourAngle>=360 else hourAngle
        
        minuteAngle = minutes*6
        angle = abs(hourAngle-minuteAngle)
        
        angle = 360-angle if angle>=180 else angle
        
        return angle
        