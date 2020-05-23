def _validate_sequence(seq, ok, issues):
    if len(seq) <= 1:
        return ok, issues
    else:
        seq_start_val = seq[0]
        for index, value in enumerate(seq):
            if value == index + seq_start_val + 1:
                issues['missing'] = issues.get(
                    'missing', []) + [index + seq_start_val]
                return _validate_sequence(seq[index:], False, issues)
            elif value != index + seq_start_val:
                issues['unexpected'] = issues.get(
                    'unexpected', []) + [{'expected': seq_start_val + index, 'actual': value}]
                next_subsequence_index = min(index + 1, len(seq) - 1)
                return _validate_sequence(seq[next_subsequence_index:], False, issues)
        return _validate_sequence([], ok, issues)


def validate_sequence(seq):
    return _validate_sequence(seq, True, dict())
