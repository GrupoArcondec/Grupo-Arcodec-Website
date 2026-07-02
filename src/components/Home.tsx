import { HeroStudio } from './studio/HeroStudio'
import { ProjectsStudio, AdvantagesStudio } from './studio/ProjectsStudio'
import { ServicesStudio, ProcessStudio } from './studio/ServicesStudio'
import { ExperienceStudio, ApproachStudio, CaseStudio } from './studio/ExperienceStudio'
import { QuoteStudio, TeamStudio } from './studio/QuoteStudio'
import { FaqStudio, BlogStudio } from './studio/FaqBlogStudio'

export function Home() {
  return (
    <main id="top" className="st-page">
      <HeroStudio />
      <ProjectsStudio />
      <AdvantagesStudio />
      <ServicesStudio />
      <ProcessStudio />
      <ExperienceStudio />
      <ApproachStudio />
      <CaseStudio />
      <QuoteStudio />
      <TeamStudio />
      <FaqStudio />
      <BlogStudio />
    </main>
  )
}
