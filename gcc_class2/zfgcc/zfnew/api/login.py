# -*- coding: utf-8 -*-
import binascii
from pprint import pprint
import rsa
import base64
import requests
from bs4 import BeautifulSoup
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from urllib import parse
from fake_useragent import UserAgent



class Login(object):
    def __init__(self, base_url):
        self.base_url = base_url
        self.key_url = parse.urljoin(base_url, '/xtgl/login_getPublicKey.html')
        self.login_url = parse.urljoin(base_url, '/xtgl/login_slogin.html')
        self.headers = {'User-Agent': str(UserAgent().random),
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                        'Referer': self.login_url}
        self.sess = requests.Session()
        self.cookies = ''
        self.cookies_str = ''

    def login(self, sid, password):
        """登陆"""
        req = self.sess.get(self.login_url, headers=self.headers)
        soup = BeautifulSoup(req.text, 'lxml')
        tokens = soup.find(id='csrftoken').get("value")

        res = self.sess.get(self.key_url, headers=self.headers).json()
        n = res['modulus']
        e = res['exponent']
        hmm = self.get_rsa(password, n, e)

        login_data = {'csrftoken': tokens,
                      'yhm': sid,
                      'mm': hmm,
                      'mm': hmm}
        response = self.sess.post(self.login_url, headers=self.headers, data=login_data)
        self.cookies = self.sess.cookies
        self.cookies_str = '; '.join([item.name + '=' + item.value for item in self.cookies])
        return response
        # return "succ"

    @classmethod
    def encrypt_sqf(cls, pkey, str_in):
        """加载公钥"""
        private_key = pkey

        private_keybytes = base64.b64decode(private_key)
        prikey = RSA.importKey(private_keybytes)

        signer = PKCS1_v1_5.new(prikey)
        signature = base64.b64encode(signer.encrypt(str_in.encode("utf-8")))
        return signature

    @classmethod
    def get_rsa(cls, pwd, n, e):
        """对密码base64编码"""
        message = str(pwd).encode()
        rsa_n = binascii.b2a_hex(binascii.a2b_base64(n))
        rsa_e = binascii.b2a_hex(binascii.a2b_base64(e))
        key = rsa.PublicKey(int(rsa_n, 16), int(rsa_e, 16))
        encropy_pwd = rsa.encrypt(message, key)
        result = binascii.b2a_base64(encropy_pwd)
        return result

