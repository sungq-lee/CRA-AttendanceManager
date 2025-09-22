from abc import ABC, abstractmethod
from mission2.module.dictionary import dictionary

class Benefit(ABC):
    @abstractmethod
    def get_days_for_benefit(self):
        pass

    @abstractmethod
    def get_benefit_point(self):
        pass


class BenefitWednesday(Benefit):
    def get_days_for_benefit(self):
        return dictionary.days_for_get_wednesday_benefit_point

    def get_benefit_point(self):
        return dictionary.wednesday_benefit_point


class BenefitWeekend(Benefit):
    def get_days_for_benefit(self):
        return dictionary.days_for_get_weekend_benefit_point

    def get_benefit_point(self):
        return dictionary.weekend_benefit_point


benefitDict = { "wednesday": BenefitWednesday(), "weekend": BenefitWeekend() }

def factory_benefit(week_day):
    instance_benefit = benefitDict.get(week_day, None)

    if instance_benefit is None:
        raise Exception("Benefit not found for week day: {}".format(week_day))

    return instance_benefit
