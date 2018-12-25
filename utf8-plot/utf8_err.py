import os
import matplotlib.pyplot as plt

n_samples = 100000
y = []

print('generating data...')
for length in range(1, 25):
    num_valid = 0
    for _ in range(n_samples):
        try:
            os.urandom(length).decode('utf8')
            num_valid += 1
        except:
            pass
    y.append(num_valid / n_samples * 100)
    print(f'{length} {y[-1]:.2f}%')

print('plotting...')
fig, ax1 = plt.subplots(figsize=(9, 5))
plt.title(f'UTF8 Validity of random byte arrays ({n_samples} samples per length)')
ax1.set_ylabel('% Of valid UTF8 strings')
ax1.set_xlabel('Length of random bytes')

ax1.plot(range(1, len(y) + 1), y, color='xkcd:red')
ax1.axis(
    xmin=1,
    xmax=len(y),
    ymin=-0.5,
    ymax=100,
)

fig.tight_layout()
plt.savefig('utf8_err.png', dpi=200)
