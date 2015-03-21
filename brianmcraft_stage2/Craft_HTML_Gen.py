
#Actual HTML from my notes
#      <div class="card-content">
#        <div class="content">
#          <div class="content-topic">
#            <span class="bold">The Basics</span>
#              <p>Reference <a href="http://www.w3schools.com/default.asp">W3 Schools</a> and <a href="http://www.google.com">Google</a> for just about anything.</p>
#              <p>Element = opening tag + content + closing tag</p>
#              <p>HTML Attributes = belong to tags<br>
#                <span class="italic">e.g. &lt;tag attribute="value"&gt;contents&lt;/tag&gt;</span>
#              <p>One great example would be a link to another site <a href="http://www.udacity.com">like this using the   <span class="bold">href</span> attribute</a> or an image using the <span class="bold">src</span> attribute:<br><br>
#                <img class="image-center-responsive" src="http://thisisinfamous.com/wp-content/uploads/2015/01/jurassic-park-logo.jpg" alt="Jurassic Park gates"><br></p>
#              <p>Just don't forget your <span class="bold">alt</span> tag; it will make someone's life better when viewing your page.</p>
#          </div>
#        </div>
#    </div>
#  <div class="content-topic-divider">
#  </div>
#    <div class="card-content">
#        <div class="icon">
#        </div>
#        <div class="content">
#          <div class="content-topic">
#            <span class="bold">Void Tags</span>
#              <p>No content, so no closing tag<br>
#            <span class="italic">e.g. Images &lt;img&gt;</span> or <span class="italic">Break &lt;br&gt;</span></p>
#          </div>
#      </div>
#    </div>



content_list = [['''The Basics''','''<p>Reference <a href="http://www.w3schools.com/default.asp">W3 Schools</a> and <a href="http://www.google.com">Google</a> for just about anything.</p>
              <p>Element = opening tag + content + closing tag</p>
              <p>HTML Attributes = belong to tags<br>
                <span class="italic">e.g. &lt;tag attribute="value"&gt;contents&lt;/tag&gt;</span>
              <p>One great example would be a link to another site <a href="http://www.udacity.com">like this using the   <span class="bold">href</span> attribute</a> or an image using the <span class="bold">src</span> attribute:<br><br>
                <img class="image-center-responsive" src="http://thisisinfamous.com/wp-content/uploads/2015/01/jurassic-park-logo.jpg" alt="Jurassic Park gates"><br></p>
              <p>Just don't forget your <span class="bold">alt</span> tag; it will make someone's life better when viewing your page.</p>'''],['''Void Tags''','''<p>No content, so no closing tag<br>
            <span class="italic">e.g. Images &lt;img&gt;</span> or <span class="italic">Break &lt;br&gt;</span></p>''']]



#This function takes a list containing parts of a topic, breaks them down, then calls the next function.
def breakdown_content_topic(content_topic):
  topic_title = content_topic[0]
  topic_notes = content_topic[1]
  return create_content_topic_html(topic_title, topic_notes)


#This function takes the individual parts of a topic, then creates all of the HTML for that topic.
def create_content_topic_html(topic_title, topic_notes):
  opening_html = '''
  <div class="card-content">
    <div class="content">
      <div class="content-topic">
        <span class="bold">''' + topic_title
  
  transition_html = '''
        </span>
          <p>''' + topic_notes

  closing_html = '''
          </p>
        </div>
      </div>
    </div>
  <div class="content-topic-divider">
  </div>'''
  content_topic_html = opening_html + transition_html + closing_html
  return content_topic_html


#This function takes a list of topics and, via the first (and thereby, second) function above, creates the content html.
def create_content_html(content_list):
  content_html = ""
  for topic in content_list:
    topic_html = breakdown_content_topic(topic)
    content_html = content_html + topic_html
  return content_html


#This assignment applies to the opening of a content card.
start_card_html = '''
<div class="card">
  <div class="card-title">
    <h3>Notes</h3>
  </div>'''

#This assignment applies to the closing of a content card.
close_card_html = '''
</div>'''


#This function creates the full HTML for a content card using the functions above.
def create_content_card_html(content_html):
  content_card_html = start_card_html + create_content_html(content_list) + close_card_html
  return content_card_html


print create_content_card_html(content_list)



