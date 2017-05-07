
import unittest

from CA_simple import get_commits, read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.txt')
        commits = get_commits(self.data)

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])
        self.assertEqual('Renamed folder to the correct name', commits[0]['commit_details'])
        self.assertEqual('2015-11-27', commits[0]['date'])
        self.assertEqual('2015', commits[0]['year'])
        self.assertEqual('Nov', commits[0]['month'])
        self.assertEqual('16:57:44', commits[0]['time_stamp'])
        
    def test_fourth_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[3]['author'])
        self.assertEqual('r1551558', commits[3]['revision'])
        self.assertEqual('Chnaged jira url to htps', commits[3]['commit_details'])
        self.assertEqual('2015-11-27', commits[3]['date'])
        self.assertEqual('2015', commits[3]['year'])
        self.assertEqual('Nov', commits[3]['month'])
        self.assertEqual('09:13:26', commits[3]['time_stamp'])
        
    def test_ninth_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Vincent', commits[8]['author'])
        self.assertEqual('r1551347', commits[8]['revision'])
        self.assertEqual('SFR-108 : removed unnecessary layouts which were copy-pasted from amx. They were enabling help_footer', commits[8]['commit_details'])
        self.assertEqual('2015-11-26', commits[8]['date'])
        self.assertEqual('2015', commits[8]['year'])
        self.assertEqual('Nov', commits[8]['month'])
        self.assertEqual('14:35:32', commits[8]['time_stamp'])
        
        
if __name__ == '__main__':
    unittest.main()
