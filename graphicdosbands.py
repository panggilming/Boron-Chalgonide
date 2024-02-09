plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams.update({'font.size': 16})

# Import data for the band structure
bands_BSe = np.loadtxt('BSe.band.gnu')

# Import data for DOS
e_BSe, dos_BSe, _ = np.loadtxt('BSe.dos', unpack=True)

# Record the values of LUMO and HOMO
Fermi = 1.9537
fig = plt.figure(figsize=(8,5))

spec = gridspec.GridSpec(ncols=2, nrows=1,
                         width_ratios=[2,1], wspace=0.2,
                         hspace=0.3)

#--------BAND STRUCTURE
ax0 = fig.add_subplot(spec[0])
k = np.unique(bands_BSe[:, 0])
bands = np.reshape(bands_BSe[:, 1], (-1, len(k)))

for band in range(len(bands)):
    ax0.plot(k, bands[band, :]-Fermi, color = 'purple', linewidth=1.5)
    ax0.set_ylim([-6,6])
    ax0.set_xlim([min(k),max(k)])


ax0.axhline(0, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)
ax0.axvline(0.5774, linewidth=0.75, color='k', alpha=0.5)
ax0.axvline(0.9107, linewidth=0.75, color='k', alpha=0.5)
ax0.set_xticks(ticks= [0, 0.5774, 0.9107, 1.5774],
                       labels=['$\Gamma$', 'M', 'K', '$\Gamma$'])
ax0.set_ylabel(r'$E-E_\mathrm{F}$ (eV)')

#--------DOS
ax1 = fig.add_subplot(spec[1])
ax1.plot(dos_BSe, e_BSe-Fermi, linewidth=1.5, color='purple')
ax1.set_ylim([-6, 6])
ax1.axhline(0, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)
ax1.set_xticks([])
ax1.set_xlim([0, 5])
ax1.set_xlabel('DOS')


plt.show()