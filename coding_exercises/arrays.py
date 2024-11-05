#!/usr/bin/python
# -*- coding: utf-8 -*-

class ArrayUtils:

    @staticmethod
    def rotate_matrix(input):
        # we can only rotate square matrices and don't have to rotate 1x1 or 0x0 matrices
        if len(input) < 2 or len(input) != len(input[0]):
            return input

        # rotate in layers
        size = len(input)
        layer = 0
        while layer < int(len(input) / 2):
            first = layer
            last = size - 1 - layer

            for i in range(first, last, 1):
                offset = i - first
                # save top left
                top = input[first][i]

                # bottom left -> top left
                input[first][i] = input[last-offset][first]

                # bottom right -> bottom left
                input[last-offset][first] = input[last][last-offset]

                # top right -> bottom right
                input[last][last-offset] = input[i][last]

                # saved top left -> top right
                input[i][last] = top

            layer += 1

        return input