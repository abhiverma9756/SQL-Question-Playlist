        i = 0
        k = 0
        j = len(nums) - 1

        while k <= j:

            if nums[k] == 0:

                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1

            elif nums[k] == 2:

                nums[k], nums[j] = nums[j], nums[k]
                j -= 1

            else:

                k += 1
