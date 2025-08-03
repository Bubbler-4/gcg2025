import os
import json
import zipfile
import importlib

def score_submission():
    scores = [0] * 400
    for test_idx in range(1, 401):
        test_filename = f'tests/task{test_idx:03}.json'
        with open(test_filename) as test_file:
            test_data = json.load(test_file)
        submission = importlib.import_module(f'submissions.task{test_idx:03}').p
        length = os.path.getsize(f'submissions/task{test_idx:03}.py')
        if all(submission(test_case['input']) == test_case['output'] for test_set in test_data.values() for test_case in test_set):
            scores[test_idx - 1] = length
    for window in range(0, 400, 20):
        if window > 0 and window % 100 == 0:
            print('---')
        cur_scores = scores[window : window + 20]
        print(''.join(str(score).ljust(4) for score in cur_scores))
    submission_score = sum(max(1, 2500 - x) if x else 0.001 for x in scores)
    print(f'Unofficial score: {submission_score:.3f}')

def pack_submission():
    with zipfile.ZipFile('submission.zip', 'w') as submission_zip:
        for test_idx in range(1, 401):
            submission_zip.write(f'submissions/task{test_idx:03}.py')

if __name__ == "__main__":
    score_submission()
    pack_submission()
