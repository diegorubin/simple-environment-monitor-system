from sems.repository.base import Base


class Monitor(Base):

    def get_position(self):
        if hasattr(self, "position"):
            return self.position
        else:
            return 0

    def ordered_by_position(self):
        return sorted(self.all(), key=lambda m: m.get_position())
