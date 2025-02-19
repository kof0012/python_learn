import os


class AES:
    def __init__(self):
        self.RoundKeys = None

    MIX_C = [
        [0x2, 0x3, 0x1, 0x1],
        [0x1, 0x2, 0x3, 0x1],
        [0x1, 0x1, 0x2, 0x3],
        [0x3, 0x1, 0x1, 0x2],
    ]
    I_MIXC = [
        [0xE, 0xB, 0xD, 0x9],
        [0x9, 0xE, 0xB, 0xD],
        [0xD, 0x9, 0xE, 0xB],
        [0xB, 0xD, 0x9, 0xE],
    ]
    RCon = [
        0x01000000,
        0x02000000,
        0x04000000,
        0x08000000,
        0x10000000,
        0x20000000,
        0x40000000,
        0x80000000,
        0x1B000000,
        0x36000000,
    ]

    S_BOX = [
        [
            0x63,
            0x7C,
            0x77,
            0x7B,
            0xF2,
            0x6B,
            0x6F,
            0xC5,
            0x30,
            0x01,
            0x67,
            0x2B,
            0xFE,
            0xD7,
            0xAB,
            0x76,
        ],
        [
            0xCA,
            0x82,
            0xC9,
            0x7D,
            0xFA,
            0x59,
            0x47,
            0xF0,
            0xAD,
            0xD4,
            0xA2,
            0xAF,
            0x9C,
            0xA4,
            0x72,
            0xC0,
        ],
        [
            0xB7,
            0xFD,
            0x93,
            0x26,
            0x36,
            0x3F,
            0xF7,
            0xCC,
            0x34,
            0xA5,
            0xE5,
            0xF1,
            0x71,
            0xD8,
            0x31,
            0x15,
        ],
        [
            0x04,
            0xC7,
            0x23,
            0xC3,
            0x18,
            0x96,
            0x05,
            0x9A,
            0x07,
            0x12,
            0x80,
            0xE2,
            0xEB,
            0x27,
            0xB2,
            0x75,
        ],
        [
            0x09,
            0x83,
            0x2C,
            0x1A,
            0x1B,
            0x6E,
            0x5A,
            0xA0,
            0x52,
            0x3B,
            0xD6,
            0xB3,
            0x29,
            0xE3,
            0x2F,
            0x84,
        ],
        [
            0x53,
            0xD1,
            0x00,
            0xED,
            0x20,
            0xFC,
            0xB1,
            0x5B,
            0x6A,
            0xCB,
            0xBE,
            0x39,
            0x4A,
            0x4C,
            0x58,
            0xCF,
        ],
        [
            0xD0,
            0xEF,
            0xAA,
            0xFB,
            0x43,
            0x4D,
            0x33,
            0x85,
            0x45,
            0xF9,
            0x02,
            0x7F,
            0x50,
            0x3C,
            0x9F,
            0xA8,
        ],
        [
            0x51,
            0xA3,
            0x40,
            0x8F,
            0x92,
            0x9D,
            0x38,
            0xF5,
            0xBC,
            0xB6,
            0xDA,
            0x21,
            0x10,
            0xFF,
            0xF3,
            0xD2,
        ],
        [
            0xCD,
            0x0C,
            0x13,
            0xEC,
            0x5F,
            0x97,
            0x44,
            0x17,
            0xC4,
            0xA7,
            0x7E,
            0x3D,
            0x64,
            0x5D,
            0x19,
            0x73,
        ],
        [
            0x60,
            0x81,
            0x4F,
            0xDC,
            0x22,
            0x2A,
            0x90,
            0x88,
            0x46,
            0xEE,
            0xB8,
            0x14,
            0xDE,
            0x5E,
            0x0B,
            0xDB,
        ],
        [
            0xE0,
            0x32,
            0x3A,
            0x0A,
            0x49,
            0x06,
            0x24,
            0x5C,
            0xC2,
            0xD3,
            0xAC,
            0x62,
            0x91,
            0x95,
            0xE4,
            0x79,
        ],
        [
            0xE7,
            0xC8,
            0x37,
            0x6D,
            0x8D,
            0xD5,
            0x4E,
            0xA9,
            0x6C,
            0x56,
            0xF4,
            0xEA,
            0x65,
            0x7A,
            0xAE,
            0x08,
        ],
        [
            0xBA,
            0x78,
            0x25,
            0x2E,
            0x1C,
            0xA6,
            0xB4,
            0xC6,
            0xE8,
            0xDD,
            0x74,
            0x1F,
            0x4B,
            0xBD,
            0x8B,
            0x8A,
        ],
        [
            0x70,
            0x3E,
            0xB5,
            0x66,
            0x48,
            0x03,
            0xF6,
            0x0E,
            0x61,
            0x35,
            0x57,
            0xB9,
            0x86,
            0xC1,
            0x1D,
            0x9E,
        ],
        [
            0xE1,
            0xF8,
            0x98,
            0x11,
            0x69,
            0xD9,
            0x8E,
            0x94,
            0x9B,
            0x1E,
            0x87,
            0xE9,
            0xCE,
            0x55,
            0x28,
            0xDF,
        ],
        [
            0x8C,
            0xA1,
            0x89,
            0x0D,
            0xBF,
            0xE6,
            0x42,
            0x68,
            0x41,
            0x99,
            0x2D,
            0x0F,
            0xB0,
            0x54,
            0xBB,
            0x16,
        ],
    ]

    I_SBOX = [
        [
            0x52,
            0x09,
            0x6A,
            0xD5,
            0x30,
            0x36,
            0xA5,
            0x38,
            0xBF,
            0x40,
            0xA3,
            0x9E,
            0x81,
            0xF3,
            0xD7,
            0xFB,
        ],
        [
            0x7C,
            0xE3,
            0x39,
            0x82,
            0x9B,
            0x2F,
            0xFF,
            0x87,
            0x34,
            0x8E,
            0x43,
            0x44,
            0xC4,
            0xDE,
            0xE9,
            0xCB,
        ],
        [
            0x54,
            0x7B,
            0x94,
            0x32,
            0xA6,
            0xC2,
            0x23,
            0x3D,
            0xEE,
            0x4C,
            0x95,
            0x0B,
            0x42,
            0xFA,
            0xC3,
            0x4E,
        ],
        [
            0x08,
            0x2E,
            0xA1,
            0x66,
            0x28,
            0xD9,
            0x24,
            0xB2,
            0x76,
            0x5B,
            0xA2,
            0x49,
            0x6D,
            0x8B,
            0xD1,
            0x25,
        ],
        [
            0x72,
            0xF8,
            0xF6,
            0x64,
            0x86,
            0x68,
            0x98,
            0x16,
            0xD4,
            0xA4,
            0x5C,
            0xCC,
            0x5D,
            0x65,
            0xB6,
            0x92,
        ],
        [
            0x6C,
            0x70,
            0x48,
            0x50,
            0xFD,
            0xED,
            0xB9,
            0xDA,
            0x5E,
            0x15,
            0x46,
            0x57,
            0xA7,
            0x8D,
            0x9D,
            0x84,
        ],
        [
            0x90,
            0xD8,
            0xAB,
            0x00,
            0x8C,
            0xBC,
            0xD3,
            0x0A,
            0xF7,
            0xE4,
            0x58,
            0x05,
            0xB8,
            0xB3,
            0x45,
            0x06,
        ],
        [
            0xD0,
            0x2C,
            0x1E,
            0x8F,
            0xCA,
            0x3F,
            0x0F,
            0x02,
            0xC1,
            0xAF,
            0xBD,
            0x03,
            0x01,
            0x13,
            0x8A,
            0x6B,
        ],
        [
            0x3A,
            0x91,
            0x11,
            0x41,
            0x4F,
            0x67,
            0xDC,
            0xEA,
            0x97,
            0xF2,
            0xCF,
            0xCE,
            0xF0,
            0xB4,
            0xE6,
            0x73,
        ],
        [
            0x96,
            0xAC,
            0x74,
            0x22,
            0xE7,
            0xAD,
            0x35,
            0x85,
            0xE2,
            0xF9,
            0x37,
            0xE8,
            0x1C,
            0x75,
            0xDF,
            0x6E,
        ],
        [
            0x47,
            0xF1,
            0x1A,
            0x71,
            0x1D,
            0x29,
            0xC5,
            0x89,
            0x6F,
            0xB7,
            0x62,
            0x0E,
            0xAA,
            0x18,
            0xBE,
            0x1B,
        ],
        [
            0xFC,
            0x56,
            0x3E,
            0x4B,
            0xC6,
            0xD2,
            0x79,
            0x20,
            0x9A,
            0xDB,
            0xC0,
            0xFE,
            0x78,
            0xCD,
            0x5A,
            0xF4,
        ],
        [
            0x1F,
            0xDD,
            0xA8,
            0x33,
            0x88,
            0x07,
            0xC7,
            0x31,
            0xB1,
            0x12,
            0x10,
            0x59,
            0x27,
            0x80,
            0xEC,
            0x5F,
        ],
        [
            0x60,
            0x51,
            0x7F,
            0xA9,
            0x19,
            0xB5,
            0x4A,
            0x0D,
            0x2D,
            0xE5,
            0x7A,
            0x9F,
            0x93,
            0xC9,
            0x9C,
            0xEF,
        ],
        [
            0xA0,
            0xE0,
            0x3B,
            0x4D,
            0xAE,
            0x2A,
            0xF5,
            0xB0,
            0xC8,
            0xEB,
            0xBB,
            0x3C,
            0x83,
            0x53,
            0x99,
            0x61,
        ],
        [
            0x17,
            0x2B,
            0x04,
            0x7E,
            0xBA,
            0x77,
            0xD6,
            0x26,
            0xE1,
            0x69,
            0x14,
            0x63,
            0x55,
            0x21,
            0x0C,
            0x7D,
        ],
    ]

    def sub_bytes(self, state):
        # 字节替换
        return [self.S_BOX[i][j] for i, j in [(_ >> 4, _ & 0xF) for _ in state]]

    def sub_bytes_inv(self, state):
        # 字节逆替换
        return [self.I_SBOX[i][j] for i, j in [(_ >> 4, _ & 0xF) for _ in state]]

    @staticmethod
    def shift_rows(s):
        # 行移位
        return [
            s[0],
            s[5],
            s[10],
            s[15],
            s[4],
            s[9],
            s[14],
            s[3],
            s[8],
            s[13],
            s[2],
            s[7],
            s[12],
            s[1],
            s[6],
            s[11],
        ]

    @staticmethod
    def shift_rows_inv(s):
        # 逆行移位
        return [
            s[0],
            s[13],
            s[10],
            s[7],
            s[4],
            s[1],
            s[14],
            s[11],
            s[8],
            s[5],
            s[2],
            s[15],
            s[12],
            s[9],
            s[6],
            s[3],
        ]

    def mix_columns(self, state):
        # 列混合
        return self.matrix_mul(self.MIX_C, state)

    def mix_columns_inv(self, state):
        # 逆列混合
        return self.matrix_mul(self.I_MIXC, state)

    @staticmethod
    def rot_word(_4byte_block):
        # 用于生成轮密钥的字移位
        return ((_4byte_block & 0xFFFFFF) << 8) + (_4byte_block >> 24)

    def sub_word(self, _4byte_block):
        # 用于生成密钥的字节替换
        result = 0
        for position in range(4):
            i = _4byte_block >> position * 8 + 4 & 0xF
            j = _4byte_block >> position * 8 & 0xF
            result ^= self.S_BOX[i][j] << position * 8
        return result

    @staticmethod
    def mod(poly, mod=0b100011011):
        # poly模多项式mod
        while poly.bit_length() > 8:
            poly ^= mod << poly.bit_length() - 9
        return poly

    @staticmethod
    def mul(poly1, poly2):
        # 多项式相乘
        result = 0
        for index in range(poly2.bit_length()):
            if poly2 & 1 << index:
                result ^= poly1 << index
        return result

    def matrix_mul(self, m1, m2):  # M1 = MIX_C  M2 = State
        # 用于列混合的矩阵相乘
        M = [0] * 16
        for row in range(4):
            for col in range(4):
                for Round in range(4):
                    M[row + col * 4] ^= self.mul(m1[row][Round], m2[Round + col * 4])
                M[row + col * 4] = self.mod(M[row + col * 4])
        return M

    def round_key_generator(self, _16bytes_key):
        # 轮密钥产生
        w = [
            _16bytes_key >> 96,
            _16bytes_key >> 64 & 0xFFFFFFFF,
            _16bytes_key >> 32 & 0xFFFFFFFF,
            _16bytes_key & 0xFFFFFFFF,
        ] + [0] * 40
        for i in range(4, 44):
            temp = w[i - 1]
            if not i % 4:
                temp = self.sub_word(self.rot_word(temp)) ^ self.RCon[i // 4 - 1]
            w[i] = w[i - 4] ^ temp

        self.RoundKeys = [
            self.num_2_16bytes(
                sum(
                    [
                        w[4 * i] << 96,
                        w[4 * i + 1] << 64,
                        w[4 * i + 2] << 32,
                        w[4 * i + 3],
                    ]
                )
            )
            for i in range(11)
        ]

    def add_round_key(self, state, round_keys, index):
        # 异或轮密钥
        return self._16bytes_xor(state, round_keys[index])

    @staticmethod
    def _16bytes_xor(_16bytes_1, _16bytes_2):
        return [_16bytes_1[i] ^ _16bytes_2[i] for i in range(16)]

    @staticmethod
    def _16bytes2num(_16bytes):
        # 16字节转数字
        return int.from_bytes(_16bytes, byteorder="big")

    @staticmethod
    def num_2_16bytes(num):
        # 数字转16字节
        return num.to_bytes(16, byteorder="big")

    def aes_encrypt(self, plaintext_list):
        state = plaintext_list
        state = self.add_round_key(state, self.RoundKeys, 0)
        for Round in range(1, 10):
            state = self.sub_bytes(state)
            state = self.shift_rows(state)
            state = self.mix_columns(state)
            state = self.add_round_key(state, self.RoundKeys, Round)
        state = self.sub_bytes(state)
        state = self.shift_rows(state)
        state = self.add_round_key(state, self.RoundKeys, 10)
        return state

    def aes_decrypt(self, ciphertext_list):
        state = ciphertext_list
        state = self.add_round_key(state, self.RoundKeys, 10)
        for Round in range(1, 10):
            state = self.shift_rows_inv(state)
            state = self.sub_bytes_inv(state)
            state = self.add_round_key(state, self.RoundKeys, 10 - Round)
            state = self.mix_columns_inv(state)
        state = self.shift_rows_inv(state)
        state = self.sub_bytes_inv(state)
        state = self.add_round_key(state, self.RoundKeys, 0)
        return state

    def encrypt_all(self, byt_text):
        byt_text = self.byt_padding(byt_text)
        ciphertext_all = bytes()
        for i in range(0, len(byt_text), 16):
            child = byt_text[i : i + 16]
            ciphertext = self.aes_encrypt(child)
            ciphertext_all += bytes(ciphertext)
        return ciphertext_all

    def decrypt_all(self, byt_text):
        plaintext_all = bytes()
        for i in range(0, len(byt_text), 16):
            child = byt_text[i : i + 16]
            plaintext = self.aes_decrypt(child)
            plaintext_all += bytes(plaintext)
        plaintext_all = self.byt_un_padding(plaintext_all)
        return plaintext_all

    @staticmethod
    def byt_padding(byt_text):
        """
        补齐
        """
        bs = 16
        bytes_length = len(byt_text)
        padding = bs - bytes_length % bs
        padding_bytes = bytes([padding]) * padding
        return byt_text + padding_bytes

    @staticmethod
    def byt_un_padding(byt_text):
        """
        去除补齐
        """
        length = len(byt_text)
        un_padding = int(byt_text[length - 1])
        return byt_text[0 : length - un_padding]

    @staticmethod
    def key_padding(_str: str):
        return (
            int.from_bytes(_str.encode(), byteorder="big")
            % 0x100000000000000000000000000000000
        )


if __name__ == "__main__":
    aes = AES()
    # key = 0xffffffffffffffffffffffffffffffff
    key = "三大思考的街坊四邻思考"
    key = aes.key_padding(key)
    aes.round_key_generator(key)
    print(aes.RoundKeys)

    # with open("/home/black/PycharmProjects/python_learn/a.py", "rb") as f:
    #     # with open("aes_2.py", "rb") as f:
    #     byt_text = f.read()
    #
    # ciphertext = aes.encrypt_all(byt_text=byt_text)
    #
    # with open("aes_2_test.py", "wb") as f:
    #     f.write(ciphertext)
    # print(ciphertext.hex())
    # plaintext = aes.decrypt_all(byt_text=ciphertext)
    # print(plaintext.decode())
    #     for i in range(0, len(byt_text), 16):
    #         child = byt_text[i: i + 16]

    #         # 加密
    #         ciphertext = aes.aes_encrypt(child, RoundKeys)
    #         f.write(bytes(ciphertext))

    #         # print('ciphertext = ' + hex(aes._16bytes2num(ciphertext)))

    # plaintext_all = bytes()
    # for i in range(0, len(byt_text), 16):
    #     child = byt_text[i: i + 16]

    #     # 解密
    #     plaintext = aes.aes_decrypt(child, RoundKeys)
    #     plaintext_all += bytes(plaintext)
    #     # print('plaintext = ' + hex(aes._16bytes2num(plaintext)))
