from os.path import abspath, dirname, join

from preggy import expect
from thumbor.config import Config
from thumbor.context import Context
from thumbor.loaders import LoaderResult
from tornado.testing import AsyncTestCase as TestCase
from tornado.testing import gen_test

from tc_multidir.loader import load

STORAGE_PATH = abspath(join(dirname(__file__), "../fixtures/images/"))


class FileLoaderTestCase(TestCase):
    def setUp(self):
        super().setUp()
        config = Config(TC_MULTIDIR_PATHS=[STORAGE_PATH])
        self.ctx = Context(config=config)

    async def load_file(self, file_name):
        return await load(self.ctx, file_name)

    @gen_test
    async def test_should_load_file(self):
        result = await self.load_file("screenshot.png")
        expect(result).to_be_instance_of(LoaderResult)
        with open(join(STORAGE_PATH, "screenshot.png"), "rb") as img:
            expect(result.buffer).to_equal(img.read())
        expect(result.successful).to_be_true()

    @gen_test
    async def test_should_load_file_with_extended_utf8(self):
        result = await self.load_file("utf8 æèëðġŒꭦ.png")
        expect(result).to_be_instance_of(LoaderResult)
        with open(join(STORAGE_PATH, "utf8 æèëðġŒꭦ.png"), "rb") as img:
            expect(result.buffer).to_equal(img.read())
        expect(result.successful).to_be_true()

    @gen_test
    async def test_should_fail_when_inexistent_file(self):
        result = await self.load_file("image_NOT.jpg")
        expect(result).to_be_instance_of(LoaderResult)
        expect(result.buffer).to_equal(None)
        expect(result.successful).to_be_false()

    @gen_test
    async def test_should_fail_when_outside_root_path(self):
        result = await self.load_file("../__init__.py")
        expect(result).to_be_instance_of(LoaderResult)
        expect(result.buffer).to_equal(None)
        expect(result.successful).to_be_false()

    @gen_test
    async def test_should_load_file_with_spaces_in_name(self):
        result = await self.load_file("image with spaces.png")
        expect(result).to_be_instance_of(LoaderResult)
        with open(join(STORAGE_PATH, "image with spaces.png"), "rb") as img:
            expect(result.buffer).to_equal(img.read())
        expect(result.successful).to_be_true()

    @gen_test
    async def test_should_load_file_with_spaces_encoded_in_name(self):
        result = await self.load_file("image%20with%20spaces.png")
        expect(result).to_be_instance_of(LoaderResult)
        with open(join(STORAGE_PATH, "image%20with%20spaces.png"), "rb") as img:
            expect(result.buffer).to_equal(img.read())
        expect(result.successful).to_be_true()
