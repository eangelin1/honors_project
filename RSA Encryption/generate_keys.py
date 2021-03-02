import rsa

(bob_pub, bob_priv) = rsa.newkeys(512)

f = open("keys.pem","w")
f.write("---BEGIN PUBLIC KEY---\n")
f.close()

f = open("keys.pem","ab")
f.write(bob_pub.save_pkcs1('PEM'))
f.close()

f = open("keys.pem","a")
f.write("---END PUBLIC KEY---\n\n")
f.write("---BEGIN PRIVATE KEY---\n")
f.close()

f = open("keys.pem","ab")
f.write(bob_priv.save_pkcs1('PEM'))
f.close()

f = open("keys.pem","a")
f.write("---END PRIVATE KEY---\n")
f.close()

f = open("keys.pem", "r")

pub_key = rsa.PublicKey.load_pkcs1(f, 'PEM')

f.close()

print(pub_key)