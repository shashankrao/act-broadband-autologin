#!/usr/bin/env ruby
###########################################################################
##
##  SEARCH MALWARE REPORT at the Virustotal Database using MD5 checksums.
##  =====================================================================
##   Information(Ver 1.1):
##   MD5 Checksum File - md5.txt (command line option)
##   Results File (auto generated)
##
##   Developer: Rishi Narang
##   Mail: crypt.elf@gmail.com
##   Web: www.nullprobe.com
##
##   Thanks: Karthik
##
###########################################################################

# Requirements
require 'net/http'
require 'uri'
require 'open-uri'

inFile = ARGV[0] || "md5.txt"  # use 1st command line arg if given, otherwise default
outFile = ARGV[1] || "md5_results.txt"  # use 2nd command line arg if given, otherwise default

puts "Input file: #{inFile}, Output file: #{outFile}" 

File.open(outFile, "a+") do |md5results|
  
  # Open md5.txt file for operation. 1 md5 per line.
  IO.foreach(inFile) { |line| md5 = line
    md5.chomp! #remove the newline character from the end.
    url = URI.parse('http://www.virustotal.com/vt/en/consultamd5')
    req = Net::HTTP::Post.new(url.path)
    req.set_form_data({'hash'=> md5, 'x'=>'106', 'y'=>'17'}, ';')
    res = Net::HTTP.new(url.host, url.port).start {|http| http.request(req) }
    case res
    when Net::HTTPSuccess, Net::HTTPRedirection
      #Good for me.
    else
      res.error!
    end
    body_re = /analisis\/[a-z0-9]*-[a-z0-9]*/ #Regular Expression to check the presence of analisis/<code> part.
    body = body_re.match(res.body)
    if body.nil?
      result = md5 << ": " << "not available." # if NIL, means the checksum was not found.
      md5results.puts(result)
      # puts result
    else
      vtotal = "http://www.virustotal.com/" << body[0]
      URI.parse(vtotal).open do |f| f.each {|l|
	  if md = (/<title>Virustotal. MD5: \S*\s*(.*)\s*<\/title>/iu).match(l) # Gets the information about the malware name from the HTML page TITLE.
          then
            result = md5 << ": " << md[1]
            md5results.puts(result)
            # puts result
          end
        }
      end
    end
  }
end

#EOF