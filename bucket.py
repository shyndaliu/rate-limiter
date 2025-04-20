import time

class Bucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate  # tokens per second
        self.last_refill_timestamp = time.time()

    def allow_request(self):
        now_time = time.time()
        elapsed = now_time - self.last_refill_timestamp
        added_tokens = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + added_tokens)
        self.last_refill_timestamp = now_time

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False
