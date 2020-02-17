from os.path import abspath, join, dirname

from unittest import TestCase
from preggy import expect

from thumbor.context import Context
from thumbor.config import Config
from thumbor.loaders.file_loader import load
from thumbor.loaders import LoaderResult

STORAGE_PATH = abspath(join(dirname(__file__), '../test/'))


class FileLoaderTestCase(TestCase):
    def setUp(self):
        config = Config(FILE_LOADER_ROOT_PATH=STORAGE_PATH)
        self.ctx = Context(config=config)

    def load_file(self, file_name):
        return load(self.ctx, file_name, lambda x: x).result()

    def test_should_load_file(self):
        result = self.load_file('screenshot.png')
        expect(result).to_be_instance_of(LoaderResult)
        expect(result.buffer).to_equal(
            open(join(STORAGE_PATH, 'screenshot.png')).read())
        expect(result.successful).to_be_true()

    def test_should_load_file_with_spaces(self):
        result = self.load_file('image with spaces.png')
        expect(result).to_be_instance_of(LoaderResult)
        expect(result.buffer).to_equal(
            open(join(STORAGE_PATH, 'image with spaces.png')).read())
        expect(result.successful).to_be_true()

    def test_should_load_file_with_extended_utf8(self):
        result = self.load_file('utf8 æèëðġŒꭦ.png')
        expect(result).to_be_instance_of(LoaderResult)
        expect(result.buffer).to_equal(
            open(join(STORAGE_PATH, 'utf8 æèëðġŒꭦ.png')).read())
        expect(result.successful).to_be_true()

    def test_should_fail_when_inexistent_file(self):
        result = self.load_file('image_NOT.jpg')
        expect(result).to_be_instance_of(LoaderResult)
        expect(result.buffer).to_equal(None)
        expect(result.successful).to_be_false()

    def test_should_fail_when_outside_root_path(self):
        result = self.load_file('../__init__.py')
        expect(result).to_be_instance_of(LoaderResult)
        expect(result.buffer).to_equal(None)
        expect(result.successful).to_be_false()

    def test_should_load_file_with_spaces_in_name(self):
        result = self.load_file('image with spaces.png')
        expect(result).to_be_instance_of(LoaderResult)
        expect(result.buffer).to_equal(
            open(join(STORAGE_PATH, 'image with spaces.png')).read())
        expect(result.successful).to_be_true()

    def test_should_load_file_with_spaces_encoded_in_name(self):
        result = self.load_file('image%20with%20spaces.png')
        expect(result).to_be_instance_of(LoaderResult)
        expect(result.buffer).to_equal(
            open(join(STORAGE_PATH, 'image%20with%20spaces.png')).read())
        expect(result.successful).to_be_true()