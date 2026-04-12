from main import ordered_each_recip

with open("cuisine_dentrassis/src/input.txt", "r") as f:
    content = [line.split('\n')[0] for line in f.readlines()]

all_recip = ordered_each_recip(content)

def compute_schedule(recips):
    events = []
    t_prep_end = 0
    t_oven_free = 0

    for r in recips:
        start_prep = t_prep_end
        end_prep = start_prep + r['prep']
        start_cuis = max(end_prep, t_oven_free)
        end_cuis = start_cuis + r['cuis']

        events.append({
            'ref': r['ref'],
            'start_prep': start_prep, 'end_prep': end_prep,
            'start_cuis': start_cuis, 'end_cuis': end_cuis
        })

        t_prep_end = end_prep
        t_oven_free = end_cuis

    return events

def build_sequence(events):
    total = max(e['end_cuis'] for e in events)
    result = []

    for t in range(0, total, 5):
        prep = next((e['ref'] for e in events if e['start_prep'] <= t < e['end_prep']), '.')
        cuis = next((e['ref'] for e in events if e['start_cuis'] <= t < e['end_cuis']), '.')
        result.append(prep + cuis)

    return ''.join(result)


planning = compute_schedule(all_recip)

build_sequence(planning)