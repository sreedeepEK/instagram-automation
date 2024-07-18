from crewai import Task
from textwrap import dedent

class MarketingAnalysisTasks:
    def product_analysis(self, agent, product_website, product_details):
        return Task(
            description=dedent(f"""\
                Analyze the given product website: {product_website}.
                Extra details provided by the customer: {product_details}.

                Focus on identifying unique features, benefits,
                and the overall narrative presented.

                Your final report should clearly articulate the
                product's key selling points, its market appeal,
                and suggestions for enhancement or positioning.
                Emphasize the aspects that make the product stand out.

                Keep in mind, attention to detail is crucial for
                a comprehensive analysis. It's currently 2024.
            """),
            agent=agent,
            expected_output="A detailed report with analysis and recommendations for product improvement, market appeal, and suggestions for enhancement or positioning."
        )

    def competitor_analysis(self, agent, product_website, product_details):
        return Task(
            description=dedent(f"""\
                Explore competitors of: {product_website}.
                Extra details provided by the customer: {product_details}.

                Identify the top 3 competitors and analyze their
                strategies, market positioning, and customer perception.

                Your final report MUST include BOTH all context about {product_website}
                and a detailed comparison to the identified competitors.
            """),
            agent=agent,
            expected_output="A comprehensive report detailing the strategies, market positioning, and customer perception of the top 3 competitors, including a detailed comparison with the given product website."
        )

    def campaign_development(self, agent, product_website, product_details):
        return Task(
            description=dedent(f"""\
                You're creating a targeted marketing campaign for: {product_website}.
                Extra details provided by the customer: {product_details}.

                To start this campaign we will need a strategy and creative content ideas.
                It should be meticulously designed to captivate and engage
                the product's target audience.

                Based on your ideas your co-workers will create the content for the campaign.

                Your final answer MUST include ideas that will resonate with the audience and
                also include ALL context you have about the product and the customer.
            """),
            agent=agent,
            expected_output="A strategic plan and creative content ideas for the marketing campaign, including all relevant context about the product and customer."
        )

    def instagram_ad_copy(self, agent):
        return Task(
            description=dedent("""\
                Craft an engaging Instagram post copy.
                The copy should be punchy, captivating, concise,
                and aligned with the product marketing strategy.

                Focus on creating a message that resonates with
                the target audience and highlights the product's
                unique selling points.

                Your ad copy must be attention-grabbing and should
                encourage viewers to take action, whether it's
                visiting the website, making a purchase, or learning
                more about the product.

                Your final answer MUST be 3 options for an ad copy for Instagram that
                not only informs but also excites and persuades the audience.
            """),
            agent=agent,
            expected_output="Three different engaging and persuasive Instagram ad copy options that highlight the product's unique selling points and encourage viewer action."
        )

    def take_photograph_task(self, agent, copy, product_website, product_details):
        return Task(
            description=dedent(f"""\
                You are working on a new campaign for a super important customer,
                and you MUST take the most amazing photo ever for an Instagram post
                regarding the product, you have the following copy:
                {copy}

                This is the product you are working with: {product_website}.
                Extra details provided by the customer: {product_details}.

                Imagine what the photo you want to take looks like and describe it in a paragraph.
                Here are some examples for you to follow:
                - High tech airplane in a beautiful blue sky in a beautiful sunset, super crisp, beautiful 4k, professional wide shot
                - The Last Supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
                - An bearded old man in the snow, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

                Think creatively and focus on how the image can capture the audience's
                attention. Don't show the actual product in the photo.

                Your final answer must be 3 options of photographs, each with 1 paragraph
                describing the photograph exactly like the examples provided above.
            """),
            agent=agent,
            expected_output="Three different photograph descriptions, each detailed in a paragraph, that creatively capture the audience's attention without showing the actual product."
        )

    def review_photo(self, agent, product_website, product_details):
        return Task(
            description=dedent(f"""\
                Review the photos you got from the senior photographer.
                Make sure they are the best possible and aligned with the product's goals,
                review, approve, ask clarifying questions or delegate follow-up work if
                necessary to make decisions. When delegating work, send the full draft
                as part of the information.

                This is the product you are working with: {product_website}.
                Extra details provided by the customer: {product_details}.

                Here are some examples of how the final photographs should look:
                - High tech airplane in a beautiful blue sky in a beautiful sunset, super crisp, beautiful 4k, professional wide shot
                - The Last Supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
                - An bearded old man in the snow, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

                Your final answer must be 3 reviewed options of photographs,
                each with 1 paragraph description following the examples provided above.
            """),
            agent=agent,
            expected_output="Three reviewed photograph options, each with a detailed paragraph description, ensuring alignment with the product's goals."
        )
