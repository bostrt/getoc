import os

import htmllistparse
import requests
from tqdm import tqdm


class Mirror:
    def __init__(self):
        self.base_url = "https://mirror.openshift.com/pub/openshift-v4/clients/ocp/"
        self.cwd, self.listing = htmllistparse.fetch_listing(self.base_url)

    def is_version_published(self, version: str) -> bool:
        for l in self.listing:
            if self._is_dir(l.name) and self._version_comp(version, l.name):
                return True
        return False

    def _is_dir(self, check: str) -> bool:
        # htmllistparse indicates directory with trailing slash
        return check.endswith("/")

    def _version_comp(self, user_input: str, check: str) -> bool:
        return user_input == check.replace("/", "")

    def download(self, version, file):
        url = os.path.join(self.base_url, version, "openshift-client-linux.tar.gz")
        resp = requests.get(url, stream=True)
        total_size_in_bytes = int(resp.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        for data in resp.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")
