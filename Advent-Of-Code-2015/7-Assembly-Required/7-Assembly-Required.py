_gates = {}  # Maps names to gates.


class BaseGate(object):
    def __init__(self, name):
        self.name = name
        self._value = None

    def evaluate(self):
        raise NotImplementedError()

    def register_constant(self, arg):
        if arg.isdigit():
            _gates[arg] = ConstantGate(arg, arg)
        return arg


class ConstantGate(BaseGate):
    def __init__(self, name, arg):
        super(ConstantGate, self).__init__(name)
        self._value = int(arg)

    def evaluate(self):
        return self._value


class UnaryGate(BaseGate):
    def __init__(self, name, arg):
        super(UnaryGate, self).__init__(name)
        self.arg = self.register_constant(arg)


class DirectGate(UnaryGate):
    def evaluate(self):
        if self._value is None:
            self._value = _gates[self.arg].evaluate()
        return self._value


class NotGate(UnaryGate):
    def evaluate(self):
        if self._value is None:
            self._value = 65535 - _gates[self.arg].evaluate()
        return self._value


class BinaryGate(BaseGate):
    def __init__(self, name, left, right):
        super(BinaryGate, self).__init__(name)
        self.left = self.register_constant(left)
        self.right = self.register_constant(right)


class AndGate(BinaryGate):
    def evaluate(self):
        if self._value is None:
            self._value = (_gates[self.left].evaluate() &
                           _gates[self.right].evaluate())
        return self._value


class OrGate(BinaryGate):
    def evaluate(self):
        if self._value is None:
            self._value = (_gates[self.left].evaluate() |
                           _gates[self.right].evaluate())
        return self._value


class LeftShiftGate(BinaryGate):
    def evaluate(self):
        if self._value is None:
            self._value = (_gates[self.left].evaluate() <<
                           _gates[self.right].evaluate())
        return self._value


class RightShiftGate(BinaryGate):
    def evaluate(self):
        if self._value is None:
            self._value = (_gates[self.left].evaluate() >>
                           _gates[self.right].evaluate())
        return self._value


def get_signal_a(rows, old_signal_a=None):
    for row in rows:
        gate_input, name = row.split(' -> ')

        if name == 'b' and old_signal_a is not None:
            _gates[name] = DirectGate(name, str(old_signal_a))
            continue

        inputs = gate_input.split()
        if len(inputs) == 1:
            _gates[name] = DirectGate(name, inputs[0])
        elif len(inputs) == 2:
            _gates[name] = NotGate(name, inputs[1])
        elif len(inputs) == 3:
            left, gate_name, right = inputs
            binary_gates = {'AND': AndGate, 'OR': OrGate,
                            'LSHIFT': LeftShiftGate, 'RSHIFT': RightShiftGate}
            binary_gate = binary_gates[gate_name]
            _gates[name] = binary_gate(name, left, right)
        else:
            print('ERROR: Too many inputs!')

    gate_a = _gates['a']
    return gate_a.evaluate()


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().split('\n')

    old_signal_a = get_signal_a(rows)

    _gates.clear()

    new_signal_a = get_signal_a(rows, old_signal_a)

    print('Before, wire a has signal %d.' % old_signal_a)
    print('After, wire a has signal %d.' % new_signal_a)


if __name__ == '__main__':
    main()