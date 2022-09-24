from VASSAL.counters import Decorator, BasicPiece


class GamePiece:
    def __init__(self, slot):
        self._piece = slot.getPiece()
        self._slot = slot
        self._traits = None
        self.make_trait_array()

    def make_trait_array(self):
        traits = []
        o = Decorator.getOutermost(self._piece)
        while True:
            traits.append(o)
            if isinstance(o, BasicPiece):
                break
            o = o.getInner()
        self._traits = traits
        self._traits.reverse()

    def get_traits_array(self):
        return self._traits

    def get_trait(self, class_type, name):
        for t in self._traits:
            if t.getClass() == class_type:
                if t.myGetType() == name:
                    return t

    def remove_trait(self, index):
        if index == 0:
            raise IndexError("Can't remove BasicPiece")

        if index + 1 > len(self._traits):
            raise IndexError(f"Trait out of range: total: {len(self._traits)}, index: {index}")

        if index + 1 < len(self._traits):
            # give the outer trait a new inner trait (which will reset the outer)
            self._traits[index + 1].setInner(self._traits[index - 1])
        # remove from the list and reset the inner link
        p = self._traits.pop(index)
        p.setInner(None)

    def add_trait(self, trait):
        last = len(self._traits) - 1
        self._traits.append(trait)
        trait.setInner(self._traits[last])
