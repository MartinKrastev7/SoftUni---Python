from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in ["MuscleCar", "SportsCar"]:
            return
        car_exists = [c for c in self.cars if c.model == model]
        if car_exists:
            raise Exception(f"Car {model} is already created!")

        car = None
        if car_type == "MuscleCar":
            car = MuscleCar(model, speed_limit)
        elif car_type == "SportsCar":
            car = SportsCar(model, speed_limit)

        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        driver_exists = [d for d in self.drivers if d.name == driver_name]
        if driver_exists:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        race_exists = [r for r in self.races if r.name == race_name]
        if race_exists:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver_exists = [d for d in self.drivers if d.name == driver_name]
        if not driver_exists:
            raise Exception(f"Driver {driver_name} could not be found!")

        driver_exists = driver_exists[0]

        car_available = [c for c in self.cars if (not c.is_taken) and c.__class__.__name__ == car_type]
        if not car_available:
            raise Exception(f"Car {car_type} could not be found!")
        car_available = car_available[-1]

        if driver_exists.car is not None:
            old_car = driver_exists.car.model
            for car in self.cars:
                if car.model == old_car:
                    car.is_taken = False

            #driver_exists.car = car_available.model
            driver_exists.car = car_available
            for car in self.cars:
                if car.model == driver_exists.car.model:
                    car.is_taken = True

            return f"Driver {driver_name} changed his car from {old_car} to {driver_exists.car.model}."
        else:
            driver_exists.car = car_available
            car_available.is_taken = True
            return f"Driver {driver_name} chose the car {driver_exists.car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        race_exists = [r for r in self.races if r.name == race_name]
        if not race_exists:
            raise Exception(f"Race {race_name} could not be found!")
        race_exists = race_exists[0]

        driver_exists = [d for d in self.drivers if d.name == driver_name]
        if not driver_exists:
            raise Exception(f"Driver {driver_name} could not be found!")
        driver_exists = driver_exists[0]

        if driver_exists.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        driver_in_race = [d for d in race_exists.drivers if d.name == driver_name]
        if driver_in_race:
            return f"Driver {driver_name} is already added in {race_name} race."
        else:
            race_exists.drivers.append(driver_exists)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race_exists = [r for r in self.races if r.name == race_name]
        if not race_exists:
            raise Exception(f"Race {race_name} could not be found!")
        race_exists = race_exists[0]
        #result = ""
        if len(race_exists.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

       # driver_speed_limit = {}
        #for driver in race_exists.drivers:
         #   speed_limit = 0
          #  for car in self.cars:
           #     if car.model == driver.car:
            #        speed_limit = car.speed_limit
             #   driver_speed_limit[driver.name] = speed_limit

        #sorted_drivers_speed_limit = dict(sorted(driver_speed_limit.items(), key=lambda kv: -kv[1]))
        #winners_count = 0

       # for key, value in sorted_drivers_speed_limit.items():
           # winners_count += 1
           # if winners_count > 3:
           #     break
          #  result += f"Driver {key} wins the {race_name} race with a speed of {value}.\n"
         #   current_driver = [d for d in race_exists.drivers if d.name == key]
        #    current_driver[0].number_of_wins += 1
                #race_exists.key.number_of_wins += 1
        result = [x for x in race_exists.drivers]
        result = sorted(result, key=lambda x: x.car.speed_limit, reverse=True)
        result = result[:3]
        for driver in result:
            driver.number_of_wins += 1

        final_string = ""

        for d in result:
            final_string += f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.\n"
        return final_string.strip()

        #return result