1. baseXX_Stego: base32隐写和base64隐写。 base32隐写已经验证可用。base64暂不确定
2. BlindWaterMark： 图片频域盲水印加解密，具体用法脚本中已给出
3. Coppersmith_howgrave_univariate: 针对rsa的攻击，在n和p的部分高位已知时，可推出p的值。从而破解rsa
4. Manchester： 曼彻斯特编解码，包括标准和差分两种。用法在脚本中给出
5. Merkle_Hellman_attack: 针对Merkle_Hellman背包问题密码体系的攻击，在已知密钥串时，可通过格基规约对密文进行破解