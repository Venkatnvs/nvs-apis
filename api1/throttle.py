from rest_framework.throttling import UserRateThrottle

class PaidUserThrottle(UserRateThrottle):
    rate = '10/min'

class UnpaidUserThrottle(UserRateThrottle):
    rate = '6/mi'
