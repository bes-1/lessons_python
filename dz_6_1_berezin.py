from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for i in range(len(TrafficLight.__color)):
            if i == 0:
                print(TrafficLight.__color[i])
                for n in range(1, 8):
                    print(f'{n} сек.')
                    sleep(1)

            elif i == 1:
                print(TrafficLight.__color[i])
                for n in range(1, 3):
                    print(f'{n} сек.')
                    sleep(1)
            elif i == 2:
                print(TrafficLight.__color[i])
                for n in range(1, 11):
                    print(f'{n} сек.')
                    sleep(1)


traffic_light = TrafficLight()
traffic_light.running()
