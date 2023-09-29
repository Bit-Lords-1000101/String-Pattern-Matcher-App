def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)

    return matches

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = naive_string_match(text, pattern)
print("Naive String Matching Algorithm:")
print(f"Pattern found at positions: {matches}")

def simulate_rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    pattern_hash = sum(ord(pattern[i]) for i in range(m))

    st.write(f"Text: {text}")
    st.write(f"Pattern: {pattern}")

    for i in range(n - m + 1):
        current_text = text[i:i + m]
        current_hash = sum(ord(current_text[j]) for j in range(m))

        st.write(f"Checking text from position {i} to {i + m}: {current_text}")
        st.write(f"Text Hash: {current_hash}")

        if current_hash == pattern_hash and current_text == pattern:
            st.write("Pattern found at position:", i)
            st.write("Pattern:", pattern)
            break
        st.write("---")
        time.sleep(1)  # Sleep for 1 second to simulate the animation

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    # Calculate hash of the pattern
    pattern_hash = sum(ord(pattern[i]) for i in range(m))

    for i in range(n - m + 1):
        # Calculate hash of the current substring of text
        text_hash = sum(ord(text[i + j]) for j in range(m))
        if text_hash == pattern_hash and text[i:i + m] == pattern:
            matches.append(i)

    return matches

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = rabin_karp(text, pattern)
print("Rabin-Karp Algorithm:")
print(f"Pattern found at positions: {matches}")

import streamlit as st
import time

# Function to measure execution time
def measure_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return result, execution_time

# Streamlit UI
st.title("String Matching Algorithms Comparison")

text = st.text_input("Enter text:")
pattern = st.text_input("Enter pattern:")

option = st.radio("Choose an option:", ["Run", "Simulation"])

if option == "Run":
    if st.button("Run"):
        st.write("Running Naive String Matching Algorithm...")
        naive_result, naive_time = measure_time(naive_string_match, text, pattern)
        st.write(f"Naive Algorithm Result: {naive_result}")
        st.write(f"Naive Algorithm Execution Time: {naive_time} seconds")

        st.write("Running Rabin-Karp Algorithm...")
        rabin_result, rabin_time = measure_time(rabin_karp, text, pattern)
        st.write(f"Rabin-Karp Algorithm Result: {rabin_result}")
        st.write(f"Rabin-Karp Algorithm Execution Time: {rabin_time} seconds")

        st.write("Algorithm Comparison:")
        if naive_result == rabin_result:
            st.write("Both algorithms found the same matches.")
        else:
            st.write("Algorithms produced different results.")




if option == "Simulation":
    st.title("Rabin-Karp Algorithm Simulation")

    text = st.text_input("Enter text:", key= 1)
    pattern = st.text_input("Enter pattern:", key= 2)

    if st.button("Run Simulation"):
        st.write("Running Rabin-Karp Algorithm Simulation...")
        simulate_rabin_karp(text, pattern)


