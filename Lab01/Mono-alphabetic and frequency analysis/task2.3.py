import re
import random
import math
import os

class MonoAlphabeticBreaker:
    def __init__(self, quadgram_file):
        self.quadgrams = {}

        with open(quadgram_file, 'r') as f:
            for line in f:
                key, count = line.split()
                self.quadgrams[key.upper()] = int(count)
        
        self.L = len(next(iter(self.quadgrams)))
        self.N = sum(self.quadgrams.values())
        
        # compute Log-Probability for english-likeness scoring
        for key in self.quadgrams:
            self.quadgrams[key] = math.log10(float(self.quadgrams[key])/self.N)
        self.floor = math.log10(0.01/self.N)

    def fitness(self, text):
        """Compute 'English-likeness' score based on Quadgrams"""
        score = 0
        for i in range(len(text)-self.L+1):
            quad = text[i:i+self.L]
            if quad in self.quadgrams:
                score += self.quadgrams[quad]
            else:
                score += self.floor
        return score

    def decrypt(self, ciphertext, key):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        table = str.maketrans(alphabet, key)
        return ciphertext.translate(table)

    def solve(self, ciphertext, iterations=1000):
        # Normalize ciphertext
        clean_cipher = re.sub('[^A-Z]', '', ciphertext.upper())
        
        best_key = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        random.shuffle(best_key)
        best_score = -99e9
        
        print(f"[*] Finding best key for given ciphertext using Hill Climbing with Random Restarts...")
        
        # Random Restart: run many times to prevent local maximum traps
        for i in range(10): 
            current_key = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            random.shuffle(current_key)
            current_score = self.fitness(self.decrypt(clean_cipher, "".join(current_key)))
            
            count = 0
            while count < 1000:
                a, b = random.sample(range(26), 2)
                child_key = parent_key = current_key[:]
                child_key[a], child_key[b] = child_key[b], child_key[a]
                
                score = self.fitness(self.decrypt(clean_cipher, "".join(child_key)))
                
                if score > current_score:
                    current_score = score
                    current_key = child_key[:]
                    count = 0
                else:
                    count += 1
            
            if current_score > best_score:
                best_score = current_score
                best_key = current_key[:]
                print(f"--- Restart {i}: Score {best_score:.2f} ---")
                print(f"Best temporary plaintext: {self.decrypt(clean_cipher, ''.join(best_key))[:60]}...")
        
        final_key = "".join(best_key)
        return final_key, self.decrypt(ciphertext.upper(), final_key)

if __name__ == "__main__":
    file_name = '2.2-cipher-text.txt'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            cipher = f.read()
        
        breaker = MonoAlphabeticBreaker('english-quadgrams.txt')
        key, plaintext = breaker.solve(cipher)
        
        print("\n" + "="*50)
        print(f"KEY FOUND: {key}")
        print(f"BEST DECRYPTED TEXT: \n{plaintext}")
        print("="*50)
        
    except FileNotFoundError:
        print(f"[!] No file found: {file_path}")
    except Exception as e:
        print(f"[!] An error occurred: {e}")