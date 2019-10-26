"""
Joseph Hurni

Download and solve the puzzle below.

puzzle.txt

puzzle.txt contains 10072 lines of length 32, all looking to be hashes of some sort

Can be downloaded from a certain website
"""
import string
import hashlib


def a_newer_approach():
    """
    not the best approach efficiency-wise to get this job done, as we are creating a new string from a list each
    iteration of the main loop, but in python there isn't an easy answer, so for experimentation this is fine.
    :return:
    """

    output_string = []
    with open("puzzle.txt", "r") as f, open("solved_it.txt", "a") as solved:
        next(f)
        for l in f.readlines():
            for c in string.printable:
                # this is the bad part, no matter what you either have to keep track of a list, or create a new string
                temp_string = "".join(output_string) + c
                hash_string = str(hashlib.md5(temp_string.encode()).hexdigest())
                if hash_string == l.strip("\n"):
                    output_string.append(c)
                    solved.write(c)
                    # print(f"awesome {output_string}")

    return output_string


def do_it_again():
    """
    same as above
    :return:
    """
    output_string = []
    with open("solved_it.txt", "r") as f, open("sha1sums_solution.txt", "w") as solved:
        next(f)
        for l in f.readlines():
            for c in string.printable:
                temp_string = "".join(output_string) + c
                hash_string = str(hashlib.sha1(temp_string.encode()).hexdigest())
                if hash_string == l.strip("\n"):
                    output_string.append(c)
                    solved.write(c)
                    # print(f"awesome {output_string}")

    return output_string


def and_again():
    """
    and also same as above
    :return:
    """
    output_string = []
    with open("sha1sums_solution.txt", "r") as f, open("sha3_256sums_solution.txt", "w") as solved:
        next(f)
        for l in f.readlines():
            for c in string.printable:
                temp_string = "".join(output_string) + c
                hash_string = str(hashlib.sha3_256(temp_string.encode()).hexdigest())
                if hash_string == l.strip("\n"):
                    output_string.append(c)
                    solved.write(c)
                    # print(f"awesome {output_string}")

    return output_string


def an_actually_nice_function(input_file, output_file, hashing_algo="md5"):
    """a function that's a little nicer to use"""

    output_string = []
    with open(input_file, "r") as f, open(output_file, "w") as solved:
        next(f)
        for l in f.readlines():
            for c in string.printable:
                temp_string = "".join(output_string) + c
                h = hashlib.new(hashing_algo)
                h.update(temp_string.encode())
                hash_string = h.hexdigest()
                if hash_string == l.strip("\n"):
                    output_string.append(c)
                    solved.write(c)
                    # print(f"awesome {output_string}")

    return output_string


if __name__ == '__main__':
    # the_wrong_approach()
    # print(a_new_approach())

    # ok after trying all this stuff to figure out if each line was a single character, i figured maybe since we started
    # with nothing ("$ echo -ne "" | md5sum => d41d8cd98f00b204e9800998ecf8427e")
    # and "grew" to W ("echo -ne "W" | md5sum => 61e9c06ea9a85a5088a499df6458d276")
    # we could keep growing our string one character at a time, matching it to the hash to get our new sentence
    # print("".join(a_newer_approach()))
    # print("".join(do_it_again()))
    # print("".join(and_again()))

    print(an_actually_nice_function("sha1sums_solution.txt", "sha3_256sums_solution.txt", "sha3_256"))

    # that seemed to do it, the string that ended up getting built (really slowly due to string concatenation, in a loop
    # in a slow language like python) read "Who designed both RC5 and MD5?" => Google => Ronald Rivest.
    # ok great, now the rest of the file contains what I found out are sha1 hashes, so applying the same logic to the
    # new file will probably help us along

    # time passes, code is copy-pasted, new hashes are calculated

    # some answers below:
    # md5 sums => "Who designed both RC5 and MD5?" => Google => Ronald Rivest
    # sha1sums => "What organization designed SHA-1" => Google => Good 'ol NSA
    # sha3_256sums => "Who co-developed both AES and SHA-3?" => Google => Joan Daemen

    # another fun problem, had a lot of wrong ideas at first, but once I figured we were just building strings,
    # the rest fell into place and actually went quite quickly
