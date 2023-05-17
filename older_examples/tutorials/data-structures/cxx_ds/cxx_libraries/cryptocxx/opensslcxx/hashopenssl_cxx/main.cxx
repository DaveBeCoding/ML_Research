#include <openssl/sha.h>
#include <iostream>
#include <iomanip>
#include <sstream>

int main() {
    // string hash
    std::string str = "Hello, world!";

    //SHA-256, (binary digit(s)), 256 bits / 8 bits -> bytes = 32 
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((unsigned char*) str.c_str(), str.length(), hash);

    // hash to str
    std::stringstream ss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (int) hash[i];
    }
    std::string hash_str = ss.str();

    // hash
    std::cout << "Hash of '" << str << "': " << hash_str << std::endl;

    return 0;
}

