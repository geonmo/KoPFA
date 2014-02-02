KoPFA
=====

KoPFA

# Install
##1. Initializing
<pre><code>
cmsrel CMSSW_5_3_12_patch1

git init
git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git
git fetch cmg-central
git config core.sparsecheckout true
</code></pre>

###IF at CERN,
<pre><code>
cp /afs/cern.ch/user/g/gpetrucc/public/CMG_PAT_V5_18_from-CMSSW_5_3_14.sparse-checkout .git/info/sparse-checkout
</code></pre>
###OR at other place,
<pre><code>
scp (CERN ID)@lxplus5.cern.ch:/afs/cern.ch/user/g/gpetrucc/public/CMG_PAT_V5_18_from-CMSSW_5_3_14.sparse-checkout .git/info/sparse-checkout

</code></pre>

## 2. Fetch, checkout and clone KoPFA
<pre><code>
git fetch origin
git checkout origin/CMG_PAT_V5_18_from-CMSSW_5_3_14
git checkout -b master
git clone git@github.com:geonmo/KoPFA.git
</code></pre>
