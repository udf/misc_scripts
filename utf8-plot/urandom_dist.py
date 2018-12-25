import os
import matplotlib.pyplot as plt

n_samples = 256 * 1000

print('Getting random data...')
data = os.urandom(n_samples)
print('Processing data...')
counts = [0] * 256
for i in data:
    counts[i] += 1

average = n_samples / 256

print('Plotting...')
fig, ax1 = plt.subplots(figsize=(9, 5))
plt.title(f'distribution of os.urandom ({n_samples} samples)')
ax1.set_ylabel('Count')
ax1.set_xlabel('Byte')

ax1.plot(range(-1, 257), [average] * 258, color='black', linewidth=0.8)
ax1.bar(range(256), counts, 0.8, color='xkcd:red')
ax1.axis(
    xmin=-1,
    xmax=256,
)

fig.tight_layout()
plt.savefig('urandom_dist.png', dpi=200)
