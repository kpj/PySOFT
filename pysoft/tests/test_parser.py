from unittest import TestCase

import os, os.path

from pysoft import SOFTFile


class TestSOFTFileHeader(TestCase):
    def setUp(self):
        self.data_dir = os.path.join('pysoft', 'tests', 'data')

        self.soft = SOFTFile(os.path.join(self.data_dir, 'GDS1099.soft'))

    def tearDown(self):
        pass

    def test_normal_file(self):
        self.assertEqual(self.soft.header['database']['database_name'], 'Gene Expression Omnibus (GEO)')

        self.assertEqual(self.soft.header['dataset']['dataset_type'], 'Expression profiling by array')
        self.assertEqual(len(self.soft.header['dataset']['subsets']), 6)
        self.assertEqual(self.soft.header['dataset']['subsets'][0]['subset_sample_id'], 'GSM37063,GSM37064,GSM37065,GSM37066,GSM37067')

    def test_gzipped_file(self):
        gz_soft = SOFTFile(os.path.join(self.data_dir, 'GDS1099.soft.gz'))

        self.assertEqual(gz_soft.header, self.soft.header)
