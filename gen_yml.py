binary = 'MonsterHunterRise.exe'
url = 'http://storage.live.com/items/207D308974C1AE6B!219969:/MonsterHunterRise.exe?authkey=AJkvzg0zYsQ5QxA'

header = "name: Analyse Binary\non:\n  workflow_dispatch:\n  push:\n\n"
env = "env:\n  binary: {}\n  url: {}\n\n".format(binary, url)

job_header = "jobs:\n"
job_base = """  analyse:
    name: Analyse Binary
    runs-on: ubuntu-22.04
    steps:
      - name: Update and Upgrade
        run: |
          sudo apt update
          sudo apt upgrade -y
          sudo apt install -y zstd curl wget
      - name: Checkout
        uses: actions/checkout@v3
        with:
          lfs: true

      - name: Download Binary
        run: |
          curl -L ${{ env.url }} -o ${{ env.binary }}
          ls -alh

      - name: start docker and analyse
        run: |
          chmod +x analysis.sh
          ls -alh
          docker run --rm --env BINARY=${{ env.binary }} --name ida-docker -p 8080:8080 -v ${{ github.workspace }}:/root/host nyamisty/docker-wine-ida:7.5sp3 /root/host/analysis.sh
          ls -la

      - name: Prepare Artifact
        run: |
          tar -cvf - ${{ env.binary }}* | zstd - -o ${{ env.binary }}.tar.zst

      - name: Artifact
        uses: actions/upload-artifact@v3
        with:
          name: ${{ env.binary }}_0
          path: ${{ env.binary }}.tar.zst
"""

job_continue = []
for i in range(35*24//6 - 1):
# for i in range(6):
    job_i = """
  analyse_continue_{}:
    needs: analyse{}
    name: Analyse Binary Continue {}
    runs-on: ubuntu-22.04
    steps:
      - name: Update and Upgrade
        run: |
          sudo apt update
          sudo apt upgrade -y
          sudo apt install -y zstd

      - name: Checkout
        uses: actions/checkout@v3

      - uses: actions/download-artifact@v3
        with:
          name: ${{{{ env.binary }}}}_{}

      - name: Prepare_download Artifact
        run: |
          zstd -d ${{{{ env.binary }}}}.tar.zst -c | tar xf -

      - name: start docker and analyse
        run: |
          chmod +x analysis.sh
          ls -alh

          STARTTIME=$(date +%s%N)
          docker run --rm --env BINARY=${{{{ env.binary }}}} --name ida-docker -p 8080:8080 -v ${{{{ github.workspace }}}}:/root/host nyamisty/docker-wine-ida:7.5sp3 /root/host/analysis.sh
          ENDTIME=$(date +%s%N)

          TIMEPASSED=$(expr $ENDTIME - $STARTTIME)
          TIMEPASSED=$(expr $TIMEPASSED / 1000000000)

          if [ $TIMEPASSED -lt 18000 ]; then
            echo "Analysis time is less than 5 hours, It should be all done!"
            exit 1
          fi

          ls -la

      - name: Prepare Artifact
        run: |
          rm -rf ${{{{ env.binary }}}}.tar.zst
          tar -cvf - ${{{{ env.binary }}}}* ida_log | zstd - -o ${{{{ env.binary }}}}.tar.zst

      - name: Artifact
        uses: actions/upload-artifact@v3
        with:
          name: ${{{{ env.binary }}}}_{}
          path: ${{{{ env.binary }}}}.tar.zst
        
    """.format(i+1, "" if i == 0 else "_continue_" + str(i), i+1, i, i+1)
    job_continue.append(job_i)

print(''.join([header, env, job_header, job_base] + job_continue))