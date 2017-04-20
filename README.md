# CITESspeciesDetect
CITESspeciesDetect is a pipeline for the rapid identification of species listed by the <a href="https://www.cites.org/">Convention on International Trade in Endangered Species of Wild Flora and Fauna</a> (CITES) in forensic samples using paired-end Illumina data. The pipeline is composed of five linked tools, and data analysis passes through 3 phases: 1) pre-processing of paired-end Illumina data involving quality trimming and filtering of reads, followed by sorting by DNA barcode, 2) Operational Taxonomic Unit (OTU) clustering by barcode, and 3) taxonomy prediction and CITES identification. CITESspeciesDetect makes use of the frequently-used software tools Cutadapt v1.9.1 (http://cutadapt.readthedocs.io/en/stable/guide.html), USEARCH v8.1.1861 (http://www.drive5.com/usearch/download.html), FASTX-toolkit (http://hannonlab.cshl.edu/fastx_toolkit/), PRINSEQ (http://prinseq.sourceforge.net/), BLAST+ (ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/), and E-utilities (ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/).
A web server with user-friendly interface to the pipeline is available from: http://decathlon-fp7.citespipe-wur.surf-hosted.nl:8080/


<strong>Disclaimer</strong>

Although the authors of this pipeline have taken care to consider exceptions such as incorrectly annotated sequence records in public databases, taxonomic synonyms, and ambiguities in the CITES appendices themselves, the user is advised that the results of this pipeline can in no way be construed as conclusive evidence for either positive or negative taxonomic identification of the contents of biological materials. The pipeline and the results it produces are provided for informational purposes only. To emphasize this point, we reproduce the disclaimer of the license under which this pipeline is released verbatim, below:

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


<strong>Dependencies</strong>

The following dependencies are required: </br>
Place your copy of usearch v8.1.1861 for linux 32 bit in /bin (http://www.drive5.com/usearch/download.html) </br>
Install cutadapt v1.9+, for installation instructions see: http://cutadapt.readthedocs.io/en/stable/installation.html </br>
For BLAST, copy the NBCI nucleotide (nt) and taxonomy (taxdb) databases into /BLASTdb (ftp://ftp.ncbi.nlm.nih.gov/blast/db/).</br>

<strong>General usage</strong>
The basic command to run the example analysis: 
```
bash RunExample
```
Modify the following parameters in RunExample to analyse your own sample using the default settings of the pipeline:</br>
```<FW_File>``` Path to forward Illumina MiSeq FASTQ file (in Illumina 1.8+ format) </br>
```<RV_File>``` Path to reverse Illumina MiSeq FASTQ file (in Illumina 1.8+ format) </br>
```<SampleName>``` Sample Name, no special characters or spaces are allowed </br>

<strong>Output files</strong> </br>
By default, the output is written to /OutputFolder. </br>
The default results table is named ```<SampleName>```_98_0.2_full.tsv </br>





